from selenium import webdriver
import csv
import time
#자동화된 크롬 창 실행
driver = webdriver.Chrome('크롤링\chromedriver.exe')
#파파고 웹페이지 접속
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)

time.sleep(3)

f = open('./my_papago.csv','w',newline='')

#CSV 파일을 작성하는 객채변수 생성
wtr = csv.writer(f)

#열 제목 작성
wtr.writerow(['영단어','번역결과'])

while True:
    keyword = input("번역할 영단어 입력하세요(0입력시 종료): ")
    if keyword == '0':
        print("번역 종료")
        break
    #영단어 입력, 번역버튼 클릭
    form = driver.find_element_by_css_selector('textarea#txtSource')
    form.send_keys(keyword)

    button = driver.find_element_by_css_selector('button#btnTranslate')
    button.click()
    time.sleep(1)

    output = driver.find_element_by_css_selector('div#txtTarget').text

    wtr.writerow([keyword,output])

    driver.find_element_by_css_selector('textarea#txtSource').clear()

driver.close()

f.close()