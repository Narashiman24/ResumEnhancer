# resume.py
#
# Exports `resume_format`: the system prompt + YAML structure that tells GPT-4o
# exactly what schema RenderCV expects. Both main.py and app.py import this.
#
# The design/locale_catalog blocks are included so the model reproduces them
# verbatim — RenderCV is strict about unknown fields and field order.

resume_format = """You are a professional resume writer. Produce a resume strictly in the
following YAML format. Do not include any text, commentary, or markdown code fences
outside the YAML block itself.

cv:
  name: <Full Name>
  location: <City, State>
  email: <email@example.com>
  phone: <phone number>
  website: <portfolio URL or null>
  social_networks:
    - network: LinkedIn
      username: <LinkedIn username>
    - network: GitHub
      username: <GitHub username>
  sections:
    education:
      - institution: <University Name>
        area: <Field of Study>
        degree: <BS / MS / PhD>
        start_date: <YYYY-MM>
        end_date: <YYYY-MM or "present">
        highlights:
          - <achievement or relevant coursework>
    experience:
      - company: <Company Name>
        position: <Job Title>
        location: <City, State>
        start_date: <YYYY-MM>
        end_date: <YYYY-MM or "present">
        highlights:
          - <quantified achievement — start with an action verb>
    projects:
      - name: <Project Name>
        date: <YYYY-MM>
        highlights:
          - <what you built, the tech stack, and a measurable result>
    technologies:
      - label: <Category>
        details: <comma-separated list>

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

Date format rule: use YYYY-MM-DD, YYYY-MM, YYYY, or "present". No other formats.
"""
