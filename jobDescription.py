import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()


def job_details_provider(job_posting_url: str) -> tuple[str, str, str]:
    """
    Fetch job details from a LinkedIn job posting URL via the RapidAPI LinkedIn API.

    Returns a (company_name, job_title, description) tuple.

    Requires RAPIDAPI_KEY to be set in your .env file.
    Get a free key at https://rapidapi.com/rockapis-rockapis-default/api/linkedin-api8
    """
    api_key = os.getenv("RAPIDAPI_KEY", "")
    if not api_key:
        raise ValueError(
            "RAPIDAPI_KEY is not set. Add it to your .env file to use URL scraping. "
            "Alternatively, paste the job description text directly."
        )

    job_id_match = re.search(r"currentJobId=(\d+)", job_posting_url)
    if not job_id_match:
        raise ValueError(
            f"Could not parse a job ID from the URL: {job_posting_url}\n"
            "Expected a URL with '?currentJobId=<number>'"
        )
    job_id = job_id_match.group(1)

    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": "linkedin-api8.p.rapidapi.com",
    }
    response = requests.get(
        "https://linkedin-api8.p.rapidapi.com/get-job-details",
        headers=headers,
        params={"id": job_id},
    ).json()

    company = response["data"]["company"]["universalName"]
    title = response["data"]["title"]
    description = response["data"]["description"]
    return company, title, description
