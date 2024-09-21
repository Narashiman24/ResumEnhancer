import tkinter as tk
from tkinter import ttk
import yaml

# Function to collect form data and generate YAML structure
def generate_yaml():
    resume_data = {
        'cv': {
            'name': entry_name.get(),
            'location': entry_location.get(),
            'email': entry_email.get(),
            'phone': entry_phone.get(),
            'website': entry_website.get(),
            'social_networks': [
                {'network': 'LinkedIn', 'username': entry_linkedin.get()},
                {'network': 'GitHub', 'username': entry_github.get()}
            ],
            'sections': {
                'education': collect_entries(education_entries),
                'experience': collect_entries(experience_entries),
                'projects': collect_entries(project_entries),
                'technologies': [
                    {'label': 'Languages', 'details': entry_languages.get()},
                    {'label': 'Technologies', 'details': entry_technologies.get()}
                ]
            }
        }
    }
    # Write to YAML
    with open('/Users/narashiman/Documents/GitHub/python_projects/ResumEnhancer/resume.yaml', 'w') as file:
        yaml.dump(resume_data, file)

def collect_entries(entries_list):
    collected = []
    for entry_set in entries_list:
        data = {key: entry.get() for key, entry in entry_set.items()}
        collected.append(data)
    return collected

# Function to add additional form fields
def add_education():
    add_fields(education_entries, ['institution', 'area', 'degree', 'start_date', 'end_date'], education_frame)

def add_experience():
    add_fields(experience_entries, ['company', 'position', 'location', 'start_date', 'end_date'], experience_frame)

def add_project():
    add_fields(project_entries, ['name', 'date'], project_frame)

# Function to dynamically add fields for each entry
def add_fields(entries_list, fields, container):
    entry_dict = {}
    for field in fields:
        label = tk.Label(container, text=field.capitalize())
        label.pack()
        entry = tk.Entry(container)
        entry.pack()
        entry_dict[field] = entry
    entries_list.append(entry_dict)

# Initialize Tkinter window
root = tk.Tk()
root.title("Resume Form")

# Create canvas and scrollbar
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame within the canvas
form_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=form_frame, anchor="nw")

# Update scroll region when the window resizes
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

form_frame.bind("<Configure>", on_frame_configure)

# Personal information section
personal_info_frame = tk.Frame(form_frame)
personal_info_frame.pack()

tk.Label(personal_info_frame, text="Name").pack()
entry_name = tk.Entry(personal_info_frame)
entry_name.pack()

tk.Label(personal_info_frame, text="Location").pack()
entry_location = tk.Entry(personal_info_frame)
entry_location.pack()

tk.Label(personal_info_frame, text="Email").pack()
entry_email = tk.Entry(personal_info_frame)
entry_email.pack()

tk.Label(personal_info_frame, text="Phone").pack()
entry_phone = tk.Entry(personal_info_frame)
entry_phone.pack()

tk.Label(personal_info_frame, text="Website").pack()
entry_website = tk.Entry(personal_info_frame)
entry_website.pack()

tk.Label(personal_info_frame, text="LinkedIn Username").pack()
entry_linkedin = tk.Entry(personal_info_frame)
entry_linkedin.pack()

tk.Label(personal_info_frame, text="GitHub Username").pack()
entry_github = tk.Entry(personal_info_frame)
entry_github.pack()

# Education section
education_frame = tk.Frame(form_frame)
education_frame.pack()

tk.Label(education_frame, text="Education").pack()
education_entries = []
add_education_button = tk.Button(education_frame, text="Add Education", command=add_education)
add_education_button.pack()

# Experience section
experience_frame = tk.Frame(form_frame)
experience_frame.pack()

tk.Label(experience_frame, text="Experience").pack()
experience_entries = []
add_experience_button = tk.Button(experience_frame, text="Add Experience", command=add_experience)
add_experience_button.pack()

# Projects section
project_frame = tk.Frame(form_frame)
project_frame.pack()

tk.Label(project_frame, text="Projects").pack()
project_entries = []
add_project_button = tk.Button(project_frame, text="Add Project", command=add_project)
add_project_button.pack()

# Technologies section
technologies_frame = tk.Frame(form_frame)
technologies_frame.pack()

tk.Label(technologies_frame, text="Languages").pack()
entry_languages = tk.Entry(technologies_frame)
entry_languages.pack()

tk.Label(technologies_frame, text="Technologies").pack()
entry_technologies = tk.Entry(technologies_frame)
entry_technologies.pack()

# Submit button to generate YAML
submit_button = tk.Button(form_frame, text="Generate CV", command=generate_yaml)
submit_button.pack()

# Set canvas scrolling properties
canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

# Start Tkinter event loop
root.mainloop()
