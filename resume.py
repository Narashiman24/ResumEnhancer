import json

my_resume = '''Niruthiya Narashiman Srinivasan
+1(470) 460 0085 | nsrinivasan3@student.gsu.edu | Atlanta, GA | linkedin.com/narashimans | Github.com/Narashiman24
EDUCATION
Bachelor’s of Computer Science, Georgia State University
Relevant Coursework: System Level Programming, Data Structures, Calc II, Probability, and Stats.
President’s List(Fall 23), Dean’s List(Spring23-Present)
PROJECTS
Facial Emotion Detector
• Created a real-time facial emotion detection system using pre-trained models, enhancing user
interaction by identifying emotions from live video feeds.
• Employed OpenCV, numpy, tensorflow, keras, and the fer library to implement and optimize the emotion
detection process.
• Successfully processed and analyzed emotions in over 1000 video frames, ensuring robust and accurate
emotion detection across diverse scenarios.
Text Sentiment Analyzer
• Developed a sentiment analysis system for IMDb movie reviews, accurately categorizing reviews as
positive, negative, or neutral.
• Used Python, nltk, and the VADER sentiment analysis model for efficient natural language processing
and sentiment scoring.
• Analyzed the sentiment of over 500 movie reviews, providing detailed sentiment insights and enhancing
data-driven decision-making.
Phone Number Locator
• Created a Python script utilizing requests and csv libraries to manage and analyze mobile phone data
from an API, ensuring accurate retrieval and storage of operator and circle information.
• Processed and analyzed data from over 10000 mobile phone numbers, achieving a 100% success rate in
retrieving and recording network and circle details, optimizing data accuracy and accessibility.
EXPERIENCE
Computer Science Tutor Oct 2023 - Present
Computer Science Dept., Georgia State University
• Tutored more than 50 students with computer science classes, including CSC1301 and CSC1302.
• Led multiple group sessions and identified the common issues with specific concepts and addressed the
issue to respective professors
• Demonstrated strong communication skills and taught complex concepts like OOP, Data Structures,
Pandas, and NumPy.
Resident Assistant Oct 2023 -
Present
• Facilitated intentional conversations and conflict resolution strategies to promote student well-being
and adherence to university policies, enhancing interpersonal communication skills
• Acting as first of contact for more than 60 students and fostering a supportive environment for diverse
student populations within University Housing
SKILLS
Technical Skills Soft Skills Python, MySQL, REST APIs, Flutter, Flask, HTML, CSS
Leadership, Communication, Conflict Resolution, Administration'''

json_data = open('schema.json','r')

resume_format = f'''You are a professional resume generator. Produce a resume in the following YAML format. The output shouddn't have anything other than the given yaml format:

cv:
  name: <Your Name>
  location: <Your Location>
  email: <Your Email>
  phone: <Your Phone>
  website: <Your Website>
  social_networks:
    - network: LinkedIn
      username: <LinkedIn Username>
    - network: GitHub
      username: <GitHub Username>
  sections:
    education:
      - institution: <Institution Name>
        area: <Field of Study>
        degree: <Degree>
        start_date: <Start Date>
        end_date: <End Date>
        highlights:
          - <Highlight 1>
          - <Highlight 2>
    experience:
      - company: <Company Name>
        position: <Position>
        location: <Location>
        start_date: <Start Date>
        end_date: <End Date>
        highlights:
          - <Highlight 1>
          - <Highlight 2>
    projects:
      - name: <Project Name>
        date: <Date>
        highlights:
          - <Highlight 1>
          - <Highlight 2>
    technologies:
      - label: <Label>
        details: <Details>

design:
  theme: mycustomtheme
  font: EB Garamond
  font_size: 12pt
  page_size: letterpaper
  color: '#004f90'
  disable_external_link_icons: false
  disable_page_numbering: false
  page_numbering_style: PAGE_NUMBER
  disable_last_updated_date: false
  header_font_size: 30 pt
  text_alignment: justified
  seperator_between_connections: ''
  use_icons_for_connections: true
  margins:
    page:
      top: 1 cm
      bottom: 1 cm
      left: 1 cm
      right: 1 cm
    section_title:
      top: 0.3 cm
      bottom: 0.2 cm
    entry_area:
      left_and_right: 0.2 cm
      vertical_between: 0.2 cm
      date_and_location_width: 4.5 cm
    highlights_area:
      top: 0.10 cm
      left: 0.4 cm
      vertical_between_bullet_points: 0.10 cm
    header:
      vertical_between_name_and_connections: 0.3 cm
      bottom: 0.3 cm
      horizontal_between_connections: 0.5 cm

locale_catalog:
  phone_number_format: national 
  date_style: "MONTH_ABBREVIATION YEAR" 
  abbreviations_for_months: # translation of the month abbreviations
    - Jan
    - Feb
    - Mar
    - Apr
    - May
    - Jun
    - Jul
    - Aug
    - Sep
    - Oct
    - Nov
    - Dec
  full_names_of_months: # translation of the full month names
    - January
    - February
    - March
    - April
    - May
    - June
    - July
    - August
    - September
    - October
    - November
    - December
  month: month      # translation of the word "month"
  months: months    # translation of the word "months"
  year: year        # translation of the word "year"
  years: years      # translation of the word "years"
  present: present  # translation of the word "present"
  to: to            # translation of the word "to"

  
Use this json schema for refrence: {json_data} Date format is Please use either YYYY-MM-DD, YYYY-MM, or YYYY format or "present"!

Make sure to use the exact YAML structure provided in exact order. Use indentation, colons, and hyphens properly to maintain valid YAML syntax. Fill in each section with appropriate resume information in a similar structured format.
'''