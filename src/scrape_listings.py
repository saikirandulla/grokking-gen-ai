import requests
from bs4 import BeautifulSoup
import csv
import time

def safe_find(soup, tag, class_name):
    element = soup.find(tag, class_=class_name)
    return element.text.strip() if element else "N/A"

def scrape_linkedin_jobs(keywords, location, num_pages):
    jobs = []
    
    for page in range(num_pages):
        url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}&start={page*25}"
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        job_listings = soup.find_all('div', class_='base-card relative w-full hover:no-underline focus:no-underline base-card--link base-search-card base-search-card--link job-search-card')
        
        for job in job_listings:
            title = safe_find(job, 'h3', 'base-search-card__title')
            company = safe_find(job, 'h4', 'base-search-card__subtitle')
            job_location = safe_find(job, 'span', 'job-search-card__location')
            link = job.find('a', class_='base-card__full-link')
            link = link['href'] if link else "N/A"
            
            description = "N/A"
            if link != "N/A":
                try:
                    job_response = requests.get(link)
                    job_soup = BeautifulSoup(job_response.content, 'html.parser')
                    description_element = job_soup.find('div', class_='show-more-less-html__markup')
                    if description_element:
                        description = description_element.text.strip()
                    else:
                        description = safe_find(job_soup, 'div', 'mt4')
                except Exception as e:
                    print(f"Error fetching job details: {e}")
            
            jobs.append({
                'Title': title,
                'Company': company,
                'Location': job_location,
                'Description': description,
                'Link': link
            })
        
        print(f"Scraped page {page + 1}")
        time.sleep(2)  # Be polite, don't overwhelm the server
    
    return jobs

def save_to_csv(jobs, filename):
    keys = jobs[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(jobs)

# Usage
keywords = 'data scientist'
location = 'United States'
num_pages = 5

jobs = scrape_linkedin_jobs(keywords, location, num_pages)
save_to_csv(jobs, 'linkedin_data_scientist_jobs.csv')

print(f"Scraped {len(jobs)} job listings and saved to linkedin_data_scientist_jobs.csv")