import requests
from bs4 import BeautifulSoup
import re


LIMIT = 50
  

def extract_pages(URL):
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')

  page_text = soup.find("div", id="searchCountPages").string
  jobs_num = int(page_text.split()[-1].rstrip("건").replace(',',''))

  if jobs_num % LIMIT == 0:
    return jobs_num//LIMIT
  else:
    return jobs_num//LIMIT+1
        

def extract_jobs(last_page, URL):
  jobs = []

  for n in range(1):
    result = requests.get(f'{URL}&start={n*LIMIT}')    
    soup = BeautifulSoup(result.text, 'html.parser')
    soup = soup.find('div', id="mosaic-provider-jobcards")
    results = soup.find_all('div', {'class': 'job_seen_beacon'})

    for result in results:
      # try:
        job = extract_job(result)
        jobs.append(job)
      # except:
      #   continue

    print(f'{n+1}/{last_page} page scraped...')

  return jobs


def extract_job(soup):
  title = soup.find('h2', {'class': 'jobTitle'}).string
  company = soup.find('span', {"class": "companyName"}).string
  location = soup.find('div', {'class':"companyLocation"}).string
  
  # print(soup.prettify())
  # jobTitle = soup.find('h2', {'class': 'jobTitle'})
  # job_id = jobTitle.a['data-jk'] if jobTitle.a else None

  hrefs = soup.find('div', "more_links").find_all('a')
  job_id = None

  if len(hrefs) == 3:
    p = re.compile('(?<=&fromjk=)\w+(?=&from)')
    m = p.findall(hrefs[2]['href'])
    job_id = m[0] if len(m) == 1 else None

  for category in (title, company, location, job_id):
    if category:
      category.replace('\u2013','').replace('\n','')

  link = f"https://kr.indeed.com/viewjob?jk={job_id}" if job_id else None

  return {
    "title": title, 
    "company": company, 
    "location": location, 
    "link": link,
  }


def get_indeed_jobs(word):
    URL = f'https://kr.indeed.com/jobs?q={word}&limit={LIMIT}&'
    last_page = extract_pages(URL)
    indeed_jobs = extract_jobs(last_page, URL)
    return indeed_jobs


# title = str(result.find('a').string)
# location = str(result.find('span', {"class": "location accessible-contrast-color-location"}).string)

#  .replace('\xa0','')
# .replace('\xfc','')
# .replace('\u2013','')
# .replace(' ','')
# .replace('\n','')
# .replace(' ','')

# .split("\n-")
# &nbsp;