from openai import OpenAI
import jobDescription as jd
from resume import *

myAPIkey = open("apikey.txt",'r')

client = OpenAI(api_key = myAPIkey.read()) #replace this with you API key.

# Set your OpenAI API key

# Function to enhance resume
def enhance_resume(job_description, resume_text):
    # Craft a prompt to guide the model
    prompt = f"""
    Given the following job description, change this given resume into some that gets selected in ats system. You are given full freedon,and give out an json format resume:

    Job Description:
    {job_description}

    Resume:
    {resume_text}
    """

    # Call the OpenAI API
    response = client.chat.completions.create(model="gpt-4", messages = [
        {"role": "user","content": prompt}
    ],  # Use 'model' instead of 'engine'
    max_tokens=1000,  # Adjust this based on the length of the response you want
    temperature=0.7 )  # Controls randomness; lower values mean more predictable output)

    # Extract the generated text
    #enhanced_text = response.choices[0].text.strip()
    # Correctly access the content of the message
    enhance_text_resume = response.choices[0].message.content
    return enhance_text_resume

def create_json_resume(job_description, enhanced_resume_plain):
    prompt = f"Given the enhanced resume for this job description: {job_description}, create a JSON format resume with this resume content: {enhanced_resume_plain}."

    response = client.chat.completions.create(model="gpt-4",  # Correct model name
    messages = [
        {"role": "user","content": prompt}
    ],
    max_tokens=1000,  # Adjust this based on the length of the response you want
    temperature=0.7 )  # Controls randomness; lower values mean more predictable output)

    json_resume = response.choices[0].text.strip()  # Fixed typo
    return json_resume


# Example usage
job_description = jd.description
resume_text = my_resume
enhanced_resume = enhance_resume(job_description, resume_text)
#my_json_resume = create_json_resume(job_description,enhanced_resume)



print(enhanced_resume)
