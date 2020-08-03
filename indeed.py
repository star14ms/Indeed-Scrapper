from bs4 import BeautifulSoup
import requests
import sys
sys.path.insert(0, r'C:\Users\danal\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages')


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
