from bs4 import BeautifulSoup
import requests


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


def extract_indeed_jobs(last_page):
  jobs = []
  for n in range(last_page):
    result = requests.get(f'{URL}jobOffset={n*LIMIT}')
    print(result.status_code)
  return jobs
