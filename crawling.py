import random
import time
import requests
from bs4 import BeautifulSoup
from urllib import parse

def crawling():
    f = open('movie.txt', "w")
    base_url = "https://movie.naver.com/movie/point/af/list.naver?&page="

    for page in range(1,100):
        url = base_url + str(page)
        res = requests.get(url)

        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'lxml')
            tds = soup.select('table.list_netizen > tbody > tr > td.title')
            for td in tds:
                movie_title = td.select_one('a.movie').text.strip()
                link = td.select_one('a.movie').get('href')
                link = parse.urljoin(base_url, link)
                score = td.select_one('div.list_netizen_score > em').text.strip()
                comment = td.select_one('br').next_sibling.strip()
                f.write(movie_title + " :: ")  # , score, comment, sep='  ::  ')
                f.write(score + " :: ")
                f.write(comment)
                f.write("\n")

            interval = round(random.uniform(0.2,1.2), 2)
            time.sleep(interval)
            print(page)
    f.close()

crawling()