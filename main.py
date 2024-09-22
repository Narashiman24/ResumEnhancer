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
    temperature=0.7 )  # Controls randomness; lower values mean more predictable output)

    # Extract the generated text
    #enhanced_text = response.choices[0].text.strip()
    # Correctly access the content of the message
    enhance_text_resume = response.choices[0].message.content
    return enhance_text_resume

#user_job_posting_url = str(input("Please enter you job url: "))

# Example usage
#job_details_output_main = jd.job_details_provider(user_job_posting_url)

hard_code_jd= f"""About the job
Company Description



Global HC Analytics LLC is a niche consulting firm based in New Jersey, specializing in healthcare data analytics for the biopharma industry (“life sciences”, biotech, pharmaceutical manufacturers, et al). We offer expertise in analyzing and interpreting data to drive informed decisions and strategies for our clients in the healthcare sector. Primarily, we are focused on data analytics, forecasting, market insights, technological consulting, and other areas of our expertise.


Role Description



This is a temporary contract role at Global HC Analytics LLC, offering a hybrid work environment with flexibility for some remote work. This hire is crucially important and will be involved in day-to-day tasks such as building an API, eventually collecting and analyzing healthcare data, conducting research on industry trends, preparing reports, and assisting in data visualization projects to support the team.


Qualifications



Experience with AWS (Amazon Web Services) is ESSENTIAL
Data Analysis, Research, Technological, Administrative, and Report Writing skills
Microsoft Office Experienced Nice but not required
Experience with data analysis and/or visualization tools preferred but not required
Strong attention to detail and critical analytical thinking
Proficiency in Microsoft Excel and/or statistical software
Ability to work both independently and in a team environment
Interest in the healthcare/biopharma industry and data analytics
Interest in a degree in Data Science, Statistics, Public Health, or a related field
Open to a short-term contract with potential for a full-time role at Global HC Analytics LLC"""


#jd.job_details_provider(user_job_posting_url) # to get job's description, title, and company name
resume_text = my_resume
enhanced_resume = enhance_resume(hard_code_jd, resume_text).lstrip('```yaml\n').rstrip('```').strip().lstrip('```')
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