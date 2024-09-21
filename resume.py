import json

my_resume = f'''Mukhil Baskaran
470-923-9619 | mbaskaran3@student.gsu.edu | mukhilbaskaran.com | linkedin.com/in/mukhil-baskaran |
github.com/mukhil0212
Education
Georgia State University Atlanta, GA
Bachelor of Science in Computer Science Expected 2025
• President’s List, Spring 2024
• GPA: 3.52
• Team Lead for a cross-functional project team, guiding peers in implementing web-based solutions.
Experience
Panther Dining - Chick-fil-A Student Software Assistant Atlanta, GA
Sep 2021 – Oct 2022
• Developed a stock inventory management system using Flask, HTML, CSS, and AWS, reducing inventory tracking
errors by 30%.
• Integrated AI/ML models for enhanced stock management, improving stock forecasting accuracy by 25%.
• Streamlined data analysis and management using Pandas and Excel, increasing operational efficiency by 20%.
• Provided customer service, managing order processing and resolving inquiries, enhancing customer satisfaction.
Tech Stack: Flask, HTML, CSS, AWS, AI/ML, Power BI, Pandas, Excel
MSV Enterprises Coimbatore, India
Data Science Intern May 2021 – Aug 2021
• Developed a linear regression model in Python to forecast product demand, increasing sales revenue by 15%.
• Created a Power BI dashboard, boosting cross-selling by 5%.
• Engineered a Python-based ETL process to integrate data from multiple sources into a SQL database, improving
data processing efficiency by 20%.
• Utilized PyTorch for clustering algorithms to identify high-value customer segments, reducing marketing costs by
8%.
Tech Stack: Python, Power BI, SQL, ETL, PyTorch
Projects
Pneumonia Detection from X-ray Images | Python, PyTorch, Keras, OpenCV Jan 2024
• Developed a Convolutional Neural Network (CNN) using PyTorch and Keras to identify signs of pneumonia from
chest X-ray images, processing a dataset of over 5,000 images.
• Implemented data augmentation techniques to improve the model’s generalization ability.
• Achieved over 90% accuracy in detecting pneumonia across various testing datasets.
Madura Creation Portfolio Website (Client Project) | React, Tailwind CSS, AWS, Vercel Nov 2023 – Feb 2024
• Designed and developed a dynamic portfolio website for Madura Creation to showcase their business services.
• Implemented responsive web design with Tailwind CSS for optimal viewing on all devices, increasing site traffic by
25%.
Football Analysis Project | YOLO, Kmeans, Optical Flow, Python, OpenCV, NumPy, Matplotlib, Pandas
• Developed a system to detect and track players, referees, and footballs in video using YOLO, enhancing object
detection accuracy by 15%.
• Implemented Kmeans for pixel segmentation and clustering to assign players to teams based on t-shirt colors,
achieving 90% precision in player assignment.
• Utilized Optical Flow to measure camera movement between frames, improving player tracking by 10%.
• Applied Perspective Transformation to represent scene depth, enabling measurement of player movements in meters
rather than pixels, increasing tracking precision by 12%.
• Calculated player speed and distance covered, providing comprehensive performance metrics and insights for team
analysis.
Technical Skills
Languages: JavaScript, TypeScript, Python, SQL, HTML/CSS, R
Frameworks: React, Flask, Django, TensorFlow, Keras, Tailwind CSS, Next.js, Node.js
Developer Tools: Git, Docker, VS Code
Libraries: pandas, NumPy, Matplotlib, OpenCV, PyTorch'''

json_data = open('schema.json','r')

resume_format_1 = f'''You are a professional resume generator. Produce a resume in the following YAML format without changing the order of elements. The output shouddn't have anything other than the given yaml format:

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

resume_format = f"""You are a professional resume generator. Produce a resume strictly in the following YAML format without any additional text or commentary:

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
  abbreviations_for_months: 
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
  full_names_of_months: 
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
  month: month
  months: months
  year: year
  years: years
  present: present
  to: to

Please ensure all sections are filled with appropriate resume information according to the structure provided. Use valid YAML syntax with correct indentation, colons, and hyphens. The date format should be YYYY-MM-DD, YYYY-MM, YYYY, or "present".
use this json schema for rules: {json_data}
"""