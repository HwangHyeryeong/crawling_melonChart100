# 필요한 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# headers.get()으로 url 정보 요청
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"}
url = "https://www.melon.com/chart/"
r = requests.get(url, headers=headers)
r.status_code

# 해당 웹페이지 크롤링
soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')  # r.text == t.content
print(soup)

# 크롤링 데이터 정보
date = soup.find("span", {"class": "year"})
time = soup.find("span", {"class": "hour"})
info = date.text + " " + time.text
print(info)

# 곡명, 가수, 앨범 정보 각각 추출
titles = soup.find_all("div", {"class": "ellipsis rank01"})
singers = soup.find_all("span", {"class": "checkEllipsis"})
albums = soup.find_all("div", {"class": "ellipsis rank03"})

# 곡 정보(순위, 곡명, 가수, 앨범명) 담을 빈 리스트 생성
rank = []
title = []
singer = []
album = []

# 빈 리스트에 필요한 정보만 담기
RANK = 100
for i in range(RANK):
    rank.append(i + 1)

for i in titles:
    title.append(i.text.strip())

for i in singers:
    singer.append(i.text.strip())

for i in albums:
    album.append(i.text.strip())

# 차트 내용 데이터프레임에 합치기
chart100 = pd.DataFrame(
    {"rank": rank,
     "singer": singer,
     "title": title,
     "album": album}
)
# 합친 데이터 프레임 출력
chart100

# 데이터프레임 csv 파일로 내보내기
chart100.to_csv('melonChart100.csv', index=False)