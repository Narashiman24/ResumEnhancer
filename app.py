"""
ResumEnhancer — Streamlit frontend
------------------------------------
Paste a job description + upload your RenderCV YAML resume →
GPT-4o rewrites it to pass ATS screening → download the rendered PDF.

Run with:
    streamlit run app.py
"""

import os
import subprocess
import glob
import yaml
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from resume import resume_format

load_dotenv()

# ── Page config ──────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="ResumEnhancer",
    page_icon="📄",
    layout="wide",
)

# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.title("⚙️ Configuration")
    st.markdown("---")

    openai_key = st.text_input(
        "OpenAI API Key",
        value=os.getenv("OPENAI_API_KEY", ""),
        type="password",
        help="Used only for this session — never stored.",
    )

    st.markdown("---")
    st.caption("Optional — only needed if you want to fetch a job description from a LinkedIn URL.")
    rapidapi_key = st.text_input(
        "RapidAPI Key (LinkedIn scraper)",
        value=os.getenv("RAPIDAPI_KEY", ""),
        type="password",
        help="[Get a free key](https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8)",
    )

    st.markdown("---")
    st.markdown(
        "**How it works**\n"
        "1. Paste a job description (or fetch from LinkedIn URL)\n"
        "2. Upload your resume YAML\n"
        "3. Click **Enhance Resume**\n"
        "4. Review the output and download the PDF"
    )

# ── Header ────────────────────────────────────────────────────────────────────

st.title("📄 ResumEnhancer")
st.caption("ATS-optimize your resume against any job description using GPT-4o + RenderCV")
st.markdown("---")

# ── Job description input ─────────────────────────────────────────────────────

st.subheader("Step 1 — Job Description")

jd_mode = st.radio(
    "Input method",
    ["Paste text", "Fetch from LinkedIn URL"],
    horizontal=True,
    label_visibility="collapsed",
)

job_description = ""

if jd_mode == "Paste text":
    job_description = st.text_area(
        "Paste the full job posting here",
        height=250,
        placeholder="Copy the job description from LinkedIn, Greenhouse, Lever, etc.",
        label_visibility="collapsed",
    )
else:
    linkedin_url = st.text_input(
        "LinkedIn job URL",
        placeholder="https://www.linkedin.com/jobs/view/?currentJobId=1234567890",
    )
    if st.button("Fetch job description"):
        if not rapidapi_key:
            st.error("A RapidAPI key is required to fetch from LinkedIn. Add it in the sidebar.")
        elif not linkedin_url.strip():
            st.error("Please enter a LinkedIn URL.")
        else:
            try:
                from jobDescription import job_details_provider
                with st.spinner("Fetching from LinkedIn..."):
                    company, title, description = job_details_provider(linkedin_url)
                st.session_state["fetched_jd"] = description
                st.session_state["fetched_title"] = f"{title} at {company}"
                st.success(f"Fetched: {title} at {company}")
            except Exception as e:
                st.error(f"Failed to fetch job description: {e}")

    if "fetched_jd" in st.session_state:
        st.caption(f"**{st.session_state.get('fetched_title', '')}**")
        job_description = st.text_area(
            "Job description (editable)",
            value=st.session_state["fetched_jd"],
            height=250,
            label_visibility="collapsed",
        )

# ── Resume YAML input ─────────────────────────────────────────────────────────

st.markdown("---")
st.subheader("Step 2 — Your Resume YAML")
st.caption(
    "Upload a [RenderCV](https://docs.rendercv.com)-compatible YAML file, "
    "or paste the contents directly. See `resume.yaml` in this repo for an example."
)

uploaded_file = st.file_uploader("Upload resume.yaml", type=["yaml", "yml"])
resume_yaml_text = st.text_area(
    "...or paste your YAML here",
    height=250,
    placeholder="cv:\n  name: Your Name\n  ...",
    label_visibility="collapsed",
)

# File upload takes priority over the text area
if uploaded_file is not None:
    resume_yaml_text = uploaded_file.read().decode("utf-8")
    st.success(f"Loaded: {uploaded_file.name}")

# ── Enhance button ────────────────────────────────────────────────────────────

st.markdown("---")

if st.button("✨ Enhance Resume", type="primary", use_container_width=True):
    # Validation
    if not openai_key:
        st.error("Please enter your OpenAI API key in the sidebar.")
        st.stop()
    if not job_description.strip():
        st.error("Please provide a job description (Step 1).")
        st.stop()
    if not resume_yaml_text.strip():
        st.error("Please upload or paste your resume YAML (Step 2).")
        st.stop()

    with st.spinner("Calling GPT-4o — this usually takes 10–20 seconds..."):
        try:
            client = OpenAI(api_key=openai_key)
            prompt = f"""
Given the following job description, optimize this resume so that it passes ATS screening.
Rewrite and tailor the resume to match the job description as closely as possible.
{resume_format}

Job Description:
{job_description}

Resume:
{resume_yaml_text}
"""
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=4000,
                temperature=0.7,
            )
            raw = response.choices[0].message.content
            # GPT-4o sometimes wraps the output in ```yaml ... ``` — strip the fences
            enhanced = raw.lstrip("```yaml\n").rstrip("```").strip().lstrip("```")
            st.session_state["enhanced_yaml"] = enhanced
            st.session_state["pdf_bytes"] = None  # reset stale PDF on each new generation
            st.success("Done! Review the output below, then render to PDF.")
        except Exception as e:
            st.error(f"OpenAI API error: {e}")

# ── Result: editable YAML + PDF rendering ────────────────────────────────────

if "enhanced_yaml" in st.session_state:
    st.markdown("---")
    st.subheader("Step 3 — Review & Download")

    edited_yaml = st.text_area(
        "Enhanced resume YAML (you can edit before rendering):",
        value=st.session_state["enhanced_yaml"],
        height=450,
    )

    col_render, col_download = st.columns([1, 1])

    with col_render:
        if st.button("🖨️ Render to PDF", use_container_width=True):
            # Validate YAML before handing it to rendercv
            try:
                yaml.safe_load(edited_yaml)
            except yaml.YAMLError as e:
                st.error(f"Invalid YAML — fix it before rendering:\n\n{e}")
                st.stop()

            # Write YAML into generated_resumes/ (relative to this script),
            # then run rendercv from the project root so mycustomtheme/ is found.
            project_root = os.path.dirname(os.path.abspath(__file__))
            output_dir = os.path.join(project_root, "generated_resumes")
            os.makedirs(output_dir, exist_ok=True)

            yaml_path = os.path.join(output_dir, "resume.yaml")
            pdf_path = os.path.join(output_dir, "enhanced_resume.pdf")

            with open(yaml_path, "w") as f:
                f.write(edited_yaml)

            with st.spinner("Running RenderCV..."):
                result = subprocess.run(
                    [
                        "rendercv", "render", yaml_path,
                        "--pdf-path", pdf_path,
                        "--dont-generate-markdown",
                        "--dont-generate-html",
                        "--dont-generate-png",
                    ],
                    capture_output=True,
                    text=True,
                    cwd=project_root,
                )

            if result.returncode != 0:
                st.error(
                    "RenderCV failed. This is usually a YAML structure issue.\n\n"
                    f"```\n{result.stderr}\n```"
                )
            else:
                # Try the explicit path first; fall back to globbing in case
                # rendercv changed the output filename
                if os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f:
                        st.session_state["pdf_bytes"] = f.read()
                else:
                    pdfs = glob.glob(os.path.join(output_dir, "**", "*.pdf"), recursive=True)
                    if pdfs:
                        with open(pdfs[0], "rb") as f:
                            st.session_state["pdf_bytes"] = f.read()
                    else:
                        st.warning("Render succeeded but PDF not found. Check the generated_resumes/ folder.")

    with col_download:
        if st.session_state.get("pdf_bytes"):
            st.download_button(
                label="⬇️ Download PDF",
                data=st.session_state["pdf_bytes"],
                file_name="enhanced_resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            st.button("⬇️ Download PDF", disabled=True, use_container_width=True)
