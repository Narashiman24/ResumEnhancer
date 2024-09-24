from openai import OpenAI
import jobDescription as jd
from resume import *
import yaml 
import os

client = OpenAI(api_key = open("apikey.txt",'r').read()) #replace this with you API key.

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
    #resume_format : the structure the output resume should follow
    #job_description(str): the input from jobDescription file that scrapes the website to get job description headless browswer.
    #resum_text(str): the plain text resume from input 

    # Call the OpenAI API
    response = client.chat.completions.create(model="gpt-4o", messages = [
        {"role": "user","content": prompt}
    ],  # Use 'model' instead of 'engine'
    max_tokens=4000,  # Adjust this based on the length of the response you want
    temperature=0.7 )  # Controls randomness; lower values mean more predictable output)
    return response.choices[0].message.content #gets the output structure and ouptut.

# Asking user's input for job posting page to get job description
'''Example usage
user_job_posting_url = str(input("Please enter you job url: "))
job_details_output_main = jd.job_details_provider(user_job_posting_url)
jd.job_details_provider(user_job_posting_url) # to get job's description, title, and company name'''



main_job_description = jd.hard_jd_text_str
resume_text = my_resume
enhanced_resume = enhance_resume(main_job_description, resume_text).lstrip('```yaml\n').rstrip('```').strip().lstrip('```')
#my_json_resume = create_json_resume(job_description,enhanced_resume)



'''try:
    with open('resume.yaml', 'w') as yaml_file:
        yaml.dump(yaml.safe_load(enhanced_resume), yaml_file)

        print(enhanced_resume)
        command = f'rendercv render "resume.yaml" --pdf-path "/Users/narashiman/Documents/GitHub/python_projects/ResumEnhancer/generated_resumes" --dont-generate-markdown --dont-generate-html --dont-generate-png'

        result = os.system(command)
except yaml.YAMLError as e:
    print(f"YAML Error: {e}")'''


#command = f'rendercv render "trail.yaml" --pdf-path "/Users/narashiman/Documents/GitHub/python_projects/ResumEnhancer/generated_resumes"  --output-folder-name "{job_details_output_main[0]}_{job_details_output_main[1]} --dont-generate-markdown --dont-generate-html --dont-generate-png"'

command = f'rendercv render "resume.yaml" --pdf-path "/Users/narashiman/Documents/GitHub/python_projects/ResumEnhancer/generated_resumes" --dont-generate-markdown --dont-generate-html --dont-generate-png'
os.system(command)