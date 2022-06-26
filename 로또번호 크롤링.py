#My first crawling code (static crawling)
import requests
import bs4

URL = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(URL)

html = bs4.BeautifulSoup(raw.text,'html.parser')

target = html.find("div",{'class':'nums'})
balls = target.find_all("span",{'class':'ball_645'})
#print(target)

print("<최근 로또 당첨번호>")
for ball in balls[:-1]:
    print("당첨번호: ",ball.text)

print("보너스번호: ",balls[-1].text)
