import time

import dateutil.utils
from bs4 import BeautifulSoup
import requests
import dateparser
import datetime


html_text = requests.get('https://www.jobs.ie/python-jobs').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('div', class_='serp-item')


def find_jobs():
    with open('posts.txt', 'w') as f:
        for job in jobs:
            job_title = job.find('h2').text.strip()
            company_name = job.find('text', class_='company-title-name').text.strip()
            posted_date = job.find('dd', class_='fa-clock-o').text.strip()
            job_link = job.find('div', class_='serp-title').a['href']

            post_age = (datetime.datetime.today() - dateparser.parse(posted_date))
            if post_age <= datetime.timedelta(days=4):
                f.write('Job title:\t\t' + job_title)
                f.write('\nCompany name:\t' + company_name)
                f.write('\nDate posted:\t' + posted_date)
                f.write('\nApply here: \t' + job_link)
                f.write('\n\n')

if __name__ == '__main__':
    find_jobs()
