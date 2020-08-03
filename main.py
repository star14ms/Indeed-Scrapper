import sys
sys.path.insert(0, r'C:\Users\danal\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.8_qbz5n2kfra8p0\LocalCache\local-packages\Python38\site-packages')

import requests
from bs4 import BeautifulSoup

from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages = extract_indeed_pages()
indeed_jobs = extract_indeed_jobs(last_indeed_pages)



