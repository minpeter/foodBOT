import time
from bs4 import BeautifulSoup
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument("disable-dev-shm-usage")
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get('http://hansei.sen.hs.kr/50669/subMenu.do')



def food(monthF, dayF):
    driver.find_element_by_link_text(f'{monthF}월 {dayF}일').click()
    time.sleep(0.3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one('table.tbType02 > tbody')
    driver.find_element_by_xpath('//*[@id="divLayerMlsvPopup"]/div/div/div/button').click()

    resultlist = []
    temp = []

    for i in table.find_all("td"):
        temp.append(i.string)

    if len(temp) == 6:
        del temp[5]
        temp.append("http://hansei.sen.hs.kr" + table.find("img")["src"])

    for i in temp:
        resultlist.append(i.strip())
    
    noimg = "http://hansei.sen.hs.kr" + '/design/template/template030/images/index_board_mlsv_03/main_school_menu_thumbnail.jpg'
    resultdict = {'time':resultlist[1],'diet':resultlist[3],'calorie':resultlist[4],'img':noimg}
    
    if len(resultlist) == 6:
        resultdict['img'] = resultlist[5]
    
    

    return resultdict
