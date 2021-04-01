import time
import datetime
import requests
from bs4 import BeautifulSoup

f = open('neisapitoken', 'r')
neisapitoken = f.readline()
f.close()

URL = f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={neisapitoken}&Type=json&plndex={1}&Size={1}&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7010911"
payload = {}

def food(y,m,d):
    dt = datetime.datetime.now()
    response = requests.get(URL+f"&MLSV_YMD={dt.strftime('%Y%m%d')}", params=payload)
    print(response.text)
    return response.text
    


#resultlist[5] 1:time 3:diet 4:calorie 5:imgsrcb """  """