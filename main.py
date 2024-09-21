from openai import OpenAI
import jobDescription as jd
from resume import *
import yaml 
import os


myAPIkey = open("apikey.txt",'r')

client = OpenAI(api_key = myAPIkey.read()) #replace this with you API key.

# Set your OpenAI API key
with open('Full_Name_CV.yaml', 'r') as file:
    prime_service = yaml.safe_load(file)
# Function to enhance resume
def enhance_resume(job_description, resume_text):
    # Craft a prompt to guide the model
    prompt = f"""
    Given the following job description, optimze this resume with given jobdescription so that passes ATS system. Makeup a reusme that matchs with job description completely.
    {resume_format}
    
    Job Description:
    {job_description}

    Resume:
    {resume_text}
    """

    # Call the OpenAI API
    response = client.chat.completions.create(model="gpt-4o", messages = [
        {"role": "user","content": prompt}
    ],  # Use 'model' instead of 'engine'
    max_tokens=4000,  # Adjust this based on the length of the response you want
    temperature=0.9 )  # Controls randomness; lower values mean more predictable output)

    # Extract the generated text
    #enhanced_text = response.choices[0].text.strip()
    # Correctly access the content of the message
    enhance_text_resume = response.choices[0].message.content
    return enhance_text_resume

user_job_posting_url = str(input("Please enter you job url: "))

# Example usage
job_details_output_main = jd.job_details_provider(user_job_posting_url)


#jd.job_details_provider(user_job_posting_url) # to get job's description, title, and company name
resume_text = my_resume
enhanced_resume = enhance_resume(job_details_output_main, resume_text).lstrip('```yaml\n').rstrip('```').strip()
#my_json_resume = create_json_resume(job_description,enhanced_resume)



try:
    with open('resume.yaml', 'w') as yaml_file:
        yaml.dump(yaml.safe_load(enhanced_resume), yaml_file, default_flow_style=False)
except yaml.YAMLError as e:
    print(f"YAML Error: {e}")


#command = f'rendercv render "trail.yaml" --pdf-path "/Users/narashiman/Documents/GitHub/python_projects/ResumEnhancer/generated_resumes"  --output-folder-name "{job_details_output_main[0]}_{job_details_output_main[1]} --dont-generate-markdown --dont-generate-html --dont-generate-png"'
command = f'rendercv render "resume.yaml" --pdf-path "/Users/narashiman/Documents/GitHub/python_projects/ResumEnhancer/generated_resumes" --dont-generate-markdown --dont-generate-html --dont-generate-png'

result = os.system(command)
