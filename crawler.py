import requests
from bs4 import BeautifulSoup

def get_latest_notice():
    url = "https://www.catholic.ac.kr/ko/campuslife/notice.do"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    notice_row = soup.select_one(".board_list tbody tr")
    if notice_row:
        title = notice_row.select_one("td.title a").text.strip()
        link = "https://www.catholic.ac.kr" + notice_row.select_one("td.title a")["href"]
        return {"title": title, "link": link}
    return None
