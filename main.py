#!/usr/bin/env python3
"""
ResumEnhancer CLI
-----------------
Optimize a RenderCV YAML resume against a job description using GPT-4o,
then render the result to PDF with RenderCV.

Usage:
    python main.py <path/to/resume.yaml>

    The script will prompt you to paste a job description interactively.
    Press Enter twice when done pasting.

Environment variables (set in .env or export before running):
    OPENAI_API_KEY   — required
"""

import os
import sys
import yaml
from dotenv import load_dotenv
from openai import OpenAI
from resume import resume_format

load_dotenv()


def enhance_resume(job_description: str, resume_text: str, client: OpenAI) -> str:
    """
    Call GPT-4o to rewrite the resume YAML to match the job description.
    Returns the enhanced YAML as a string with any markdown fences stripped.
    """
    prompt = f"""
Given the following job description, optimize this resume so that it passes ATS screening.
Rewrite the resume to match the job description as closely as possible.
{resume_format}

Job Description:
{job_description}

Resume:
{resume_text}
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=4000,
        temperature=0.7,
    )
    raw = response.choices[0].message.content
    # GPT-4o sometimes wraps the output in a ```yaml ... ``` block — strip those fences
    return raw.lstrip("```yaml\n").rstrip("```").strip().lstrip("```")


def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY is not set.")
        print("Add it to a .env file in this directory or run: export OPENAI_API_KEY=sk-...")
        sys.exit(1)

    if len(sys.argv) < 2:
        print(f"Usage: python {os.path.basename(sys.argv[0])} <resume.yaml>")
        sys.exit(1)

    resume_path = sys.argv[1]
    if not os.path.exists(resume_path):
        print(f"ERROR: File not found: {resume_path}")
        sys.exit(1)

    with open(resume_path, "r") as f:
        resume_text = f.read()

    print("Paste the job description below. Press Enter twice when done:\n")
    lines = []
    while True:
        line = input()
        if line == "" and lines and lines[-1] == "":
            break
        lines.append(line)
    job_description = "\n".join(lines[:-1]).strip()

    if not job_description:
        print("ERROR: No job description provided.")
        sys.exit(1)

    client = OpenAI(api_key=api_key)
    print("\nCalling GPT-4o — this may take a few seconds...")
    enhanced = enhance_resume(job_description, resume_text, client)

    # Validate YAML before writing to disk
    try:
        yaml.safe_load(enhanced)
    except yaml.YAMLError as e:
        print(f"\nWARNING: GPT-4o returned invalid YAML — you may need to fix it manually.")
        print(f"Details: {e}")

    # Write the enhanced YAML to generated_resumes/
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated_resumes")
    os.makedirs(output_dir, exist_ok=True)

    output_yaml = os.path.join(output_dir, "resume.yaml")
    with open(output_yaml, "w") as f:
        f.write(enhanced)
    print(f"\nSaved enhanced YAML to: {output_yaml}")

    # Render the YAML to PDF using RenderCV
    print("Rendering PDF with RenderCV...")
    output_pdf = os.path.join(output_dir, "enhanced_resume.pdf")
    result = os.system(
        f'rendercv render "{output_yaml}"'
        f' --pdf-path "{output_pdf}"'
        f" --dont-generate-markdown --dont-generate-html --dont-generate-png"
    )
    if result == 0:
        print(f"PDF saved to: {output_pdf}")
    else:
        print("ERROR: RenderCV failed. Check the YAML for formatting issues.")
        sys.exit(1)


if __name__ == "__main__":
    main()
