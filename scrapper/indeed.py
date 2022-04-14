import requests
from bs4 import BeautifulSoup

LIMIT = 50
  
def extract_pages(URL):
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')

  page_text = soup.find("div", id="searchCountPages").string
  jobs_num = int(page_text.split(" ")[-1].rstrip("건"))

  if jobs_num % LIMIT == 0:
    return jobs_num//LIMIT
  else:
    return jobs_num//LIMIT+1
        
  # pagination = soup.find('ul', {'class': 'pagination-list'})
  # links = pagination.find_all('span', {'class': 'pn'})

  # pages = [] 
  # for link in links[:-1]:
  #   pages.append(int(link.string))
  # max_page = pages[-1]
  # # print(pages)
  # return max_page

def extract_jobs(last_page, URL):
  jobs = []
  for n in range(last_page):
    result = requests.get(f'{URL}&start={n*LIMIT}')    
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class': "jobsearch-SerpJobCard"})
    
    for result in results:
      title = result.find('a')["title"]

      company = result.find('span', {"class": "company"})
      if company.find('a') != None:
        company = company.find('a').string
      else:
        company = company.string
      company = company.replace('\n','')

      location = result.find('div', {'class':"recJobLoc"})['data-rc-loc']

      
      job_id = result["data-jk"]
      link = f"https://kr.indeed.com/viewjob?jk={job_id}"

      for category in (title, company, location, job_id):
        category.replace('\u2013','').replace('\n','')

      jobs.append({"title":title, "company":company, "location":location, "link":link})
    print(f'{n+1}/{last_page} page scraped...')
  return jobs

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