# stackoverflkow 직업

import requests
from bs4 import BeautifulSoup

def extract_stack_pages(URL):
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, 'html.parser')

  pagination = soup.find('div', {'class': 's-pagination'})
  links = pagination.find_all('span')
  # links = pagination.find_all('a')
  # print(links)
  # print(links[:-3])
  pages = []
  for link in links[:-3]:
    # print(link["title"])
    pages.append(int(link.string))
  max_page = pages[-1]
  return max_page


def extract_stack_jobs(last_page, URL):
  jobs = []
  for n in range(last_page):
    result = requests.get(f'{URL}&pg={n+1}')    
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all('div', {'class': "grid--cell fl1"})

    for result in results:
      title = result.h2.a['title']
      # print(title)
      # company = result.h3.find('span').string.strip()
      # print(company)
      # location = result.find('span', {'class':"fc-black-500"}).string.strip()
      company, location = result.h3.find_all("span", recursive=False)
      company = company.get_text(strip=True)
      location = location.get_text(strip=True).strip("-").strip(" /r").strip("\n")
 
      URL_2 = result.h2.a["href"]
      link = f"https://stackoverflow.com{URL_2}"

      jobs.append([title, company, location, link])
    print(f'{n+1}/{last_page} page scraped...')
  return jobs

def get_so_jobs(word):
    URL = f'https://stackoverflow.com/jobs?q={word}&sort=i'
    last_page = extract_stack_pages(URL)
    stack_jobs = extract_stack_jobs(last_page, URL)
    return stack_jobs