from selenium import webdriver
import time # 시간지연(데이터 받기와 크롬창의 로딩의 차이가 있으면안됨)
driver = webdriver.Chrome("C:/Users/Mi/Desktop/파이썬/개념/크롤링/chromedriver.exe")

URL="https://papago.naver.com/"
driver.get(URL)
time.sleep(3)

question = input("번역할 영단어를 입력하세요: ")

form =driver.find_element_by_css_selector('textarea#txtSource')#태그와 선택자를 입력받고 HTML요소를 리턴
form.send_keys(question)

button = driver.find_element_by_css_selector('button#btnTranslate')
button.click()

time.sleep(2)

result = driver.find_element_by_css_selector('div#txtTarget')
print(question,'->',result.text)

driver.close()