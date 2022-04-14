import requests
from bs4 import BeautifulSoup


LIMIT = 20
URL = 'https://www.indeed.jobs/career/SearchJobs/?'


def extract_indeed_pages():
  result = requests.get(URL)

  soup = BeautifulSoup(result.text, 'html.parser')

  pagination = soup.find('div', {'class': 'listPagination'})

  links = pagination.find_all('a')
  links = links[0:-1]

  pages = []
  for link in links:
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page

# def extract_indeed_jobs(last_page):
#   jobs = ''
#   for n in range(last_page):
#     result = requests.get(f'{URL}jobOffset={n*LIMIT}')
#     soup = BeautifulSoup(result.text, 'html.parser')
#     results = soup.find_all('li', {'class': 'listSingleColumnItem'})
#     for result in results:
#       job = str((result.find('a').string) + '\n')
#       print(job)
#       jobs = jobs + job
#       # print(job.replace(' ','').replace(',',', ').replace('-',' - '))
#     print(f'{n+1}/{last_page} page scraped...')
#   print('\n')
#   return jobs

def extract_indeed_jobs(last_page):
  jobs = []
  for n in range(last_page):
    result = requests.get(f'{URL}jobOffset={n*LIMIT}')
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('li', {'class': 'listSingleColumnItem'})
    for result in results:
      job = result.find('a').string
      title, location = job.replace('\xa0','').replace('\xfc','').replace('\u2013','').replace(' ','').split("\n-")
      location = location.replace('\n','')
      jobs.append([title, location])
    print(f'{n+1}/{last_page} page scraped...')
  print(jobs)
  return jobs

# .replace('\n','').replace(' ','')
