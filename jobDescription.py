import requests
import re

def job_details_provider(job_posting_url):

    url = "https://linkedin-api8.p.rapidapi.com/get-job-details"

    job_id = re.search(r'currentJobId=(\d+)', job_posting_url).group(1)
    
    headers = {
	"x-rapidapi-key": open("rapidapi_api_key.txt",'r').read(),
	"x-rapidapi-host": "linkedin-api8.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params={"id":job_id}).json()
    return (response['data']['company']['universalName'],response['data']['title'],response['data']['description'])

