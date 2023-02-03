# LinkedIn API Testing
from linkedin_api import Linkedin
from credentials import email, password


def open_jobs(role, location, num):

    # Authenticate using any LinkedIn account credentials
    api = Linkedin(email, password)

    jobs = api.search_jobs(role, location)

    print('Total Jobs: ', len(jobs))

    scrapped_jobs = []
    for i in range(num):
        details = api.get_job(jobs[i]['entityUrn'].split(":")[-1])
        Title = details['title']
        Company = details['companyDetails']['com.linkedin.voyager.deco.jobs.web.shared.WebCompactJobPostingCompany']['companyResolutionResult']['name']
        Location = details['formattedLocation']
        Job_Link = f"https://www.linkedin.com/jobs/view/{jobs[i]['entityUrn'].split(':')[-1]}"
        Description = details['description']['text']

        scrapped_jobs.append([Title, Company, Location, Job_Link, Description])

    return scrapped_jobs

