import time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.get('http://hansei.sen.hs.kr/50649/subMenu.do')


def food(monthF, dayF):
    driver.find_element_by_link_text(f'{monthF}월 {dayF}일').click()
    time.sleep(0.3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one('table.tbType02 > tbody')
    driver.find_element_by_xpath('//*[@id="divLayerMlsvPopup"]/div/div/div/button').click()

    resultlist = []

    for i in table.find_all("td"):
        result = i.string
        resultlist.append(result)

    if len(resultlist) == 6:
        del resultlist[5]
        resultlist.append(table.find("img")["src"])

    return resultlist

#resultlist[5] 1:time 3:diet 4:calorie 5:imgsrc