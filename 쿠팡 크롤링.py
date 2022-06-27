import requests
import bs4

while True:
    keyword = input("Enter product name(In Gmarket): ")
    print("Quit if you enter 0")
    if keyword =='0':
        break

    URL = 'https://browse.gmarket.co.kr/search?keyword='+keyword
    raw = requests.get(URL)

    html = bs4.BeautifulSoup(raw.text,'html.parser')


    box = html.find('div',{'class':'section__inner-content-body'})
    items = box.find_all('div',{'class':'box__item-container'})

    print("Gmarket",keyword,"product information")
    for item in items[:10]:
        title = item.find('span',{'class':'text__item'})
        price = item.find('strong',{'class':'text__value'})
        print('이름: ',title.text)
        print('가격: ',price.text)