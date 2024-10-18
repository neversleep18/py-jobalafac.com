import requests
from bs4 import BeautifulSoup

def scrape_indeed(keyword):
    url = f"https://fr.indeed.com/jobs?q={keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    jobs = []
    for job in soup.find_all('div', class_='jobsearch-ResultsList'):
        title = job.find('h2', class_='jobTitle').text.strip()
        company = job.find('span', class_='companyName').text.strip()
        jobs.append({'title': title, 'company': company})
    
    return jobs

# Fonctions similaires pour Monster et Welcome to the Jungle
