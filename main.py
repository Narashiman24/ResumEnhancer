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
    Given the following job description, optimze this resume with given jobdescription so that passes ATS system. if there null value use an random value but follow the json schema
    {resume_format}
    
    Job Description:
    {job_description}

    Resume:
    {resume_text}
    """

    # Call the OpenAI API
    response = client.chat.completions.create(model="gpt-4", messages = [
        {"role": "user","content": prompt}
    ],  # Use 'model' instead of 'engine'
    max_tokens=2000,  # Adjust this based on the length of the response you want
    temperature=0.4 )  # Controls randomness; lower values mean more predictable output)

    # Extract the generated text
    #enhanced_text = response.choices[0].text.strip()
    # Correctly access the content of the message
    enhance_text_resume = response.choices[0].message.content
    return enhance_text_resume


# Example usage
job_description = jd.description
resume_text = my_resume
enhanced_resume = enhance_resume(job_description, resume_text)
#my_json_resume = create_json_resume(job_description,enhanced_resume)



rs = yaml.safe_load(enhanced_resume)

with open('trail.yaml', 'w') as file:
    yaml.dump(rs, file)

command = 'rendercv render "trail.yaml" --pdf-path "/Users/narashiman/Documents/GitHub/python_projects/ResumEnhancer"'

result = os.system(command)
