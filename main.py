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
job_details_output_main = f'''About the job
Job Category: Intern/Co-op

Time Type: Part time

Minimum Clearance Required to Start: TS/SCI

Employee Type: Part-Time On-Call

Percentage of Travel Required: None

Type of Travel: None

* * *

The Opportunity

Based on CACI’s principles of integrity, commitment, distinction, and pride, our culture defines who we are, how we act, and what we believe is the right way to do business. We’re seeking an innovative Software Engineering intern to join our Sarasota, FL team for the summer of 2025, with the potential for a full-time position after the internship. The internship will begin in May and last 10-12 weeks, you will be expected to work 100% on-site at our Sarasota, FL location.

If you would enjoy the opportunity to work on a large, long term, program that meets real-world challenges, this may be a good fit for you. We implement our projects as small innovative teams. This arrangement will offer you and your teammates the maximum opportunity for contribution, and exchange of solutions and technologies.

Responsibilities

Collaboratively create mission critical software applications for its users, whom we coordinate with heavily for design and development to ensure we bring the right product to make our users efficient and effective in the execution of their mission
Have excellent learning opportunities, be highly self-directed and motivated, and collaborate respectfully with your teammates, always keeping user mission first
Be part of a responsive team where communication skills and the ability to solve problems are critical to our success
Work with highly motivated teammates that will support and push you and will expect reciprocal action on your part
Contribute to a culture of open communication amongst teammates and management team 
Be dedicated to mission and product success 
Write clean and testable code that is compliant with the design and interface definitions
Provide support to test, integrate, and deploy the software baseline
Be self-motivated to learn technical concepts, have good communication skills, and be able and willing to collaborate on technical items with the larger team

Qualifications

Required: 

Currently pursuing a Bachelor’s or Master’s degree in Computer Science, Software Engineering, Electrical Engineering or a related field
Must be legally authorized to work in the United States without the need for employer sponsorship, now or at any time in the future
Must be able to obtain and maintain applicable security clearance
Experience with a JavaScript front-end framework (Vue/Angular/React) 
Experience with both Object Oriented and Functional Programming approaches 
Experience with HTML/CSS 
Experience with UX design principles 
Experience with REST 
Experience with Git

Desired

Experience with TypeScript 
Experience with a JavaScript testing framework (Vitest, Jest, Playwright, etc.) 
Experience with Linux operating systems 
Familiarity with CI/CD Pipelines

______________________________________________________________________________

What You Can Expect

A culture of integrity.

At CACI, we place character and innovation at the center of everything we do. As a valued team member, you’ll be part of a high-performing group dedicated to our customer’s missions and driven by a higher purpose – to ensure the safety of our nation.

An environment of trust.

CACI takes pride in fostering a diverse and accessible culture where every individual feels supported to chart their own path. You’ll have the autonomy to take the time you need through a unique flexible time off benefit and have access to robust learning resources to make your ambitions a reality.

A focus on continuous growth.

Together, we will advance our nation's most critical missions, build on our lengthy track record of business success, and find opportunities to break new ground — in your career and in our legacy.

Your potential is limitless. So is ours.

Learn more about CACI here.

______________________________________________________________________________

Pay Range: There are a host of factors that can influence final salary including, but not limited to, geographic location, Federal Government contract labor categories and contract wage rates, relevant prior work experience, specific skills and competencies, education, and certifications. Our employees value the flexibility at CACI that allows them to balance quality work and their personal lives. We offer competitive compensation, benefits and learning and development opportunities. Our broad and competitive mix of benefits options is designed to support and protect employees and their families. At CACI, you will receive comprehensive benefits such as; healthcare, wellness, financial, retirement, family support, continuing education, and time off benefits. Learn more here.

The Proposed Salary Range For This Position Is

$35,776 - $69,000

CACI is an Equal Opportunity/Affirmative Action Employer. All qualified applicants will receive consideration for employment without regard to race, color, religion, sex, pregnancy, sexual orientation, gender identity, age, national origin, disability, status as a protected veteran, or any other protected characteristic.
'''#jd.job_details_provider(user_job_posting_url) # to get job's description, title, and company name
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
