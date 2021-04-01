import time
import datetime
import requests
import json

f = open('neisapitoken', 'r')
neisapitoken = f.readline()
f.close()

URL = f"https://open.neis.go.kr/hub/mealServiceDietInfo?KEY={neisapitoken}&Type=json&plndex={1}&Size={1}&ATPT_OFCDC_SC_CODE=B10&SD_SCHUL_CODE=7010911"

def food(m,d):
    dt = datetime.datetime.now()
    response = requests.get(URL+f"&MLSV_YMD={dt.strftime('%Y%m%d')}").json()
    print(URL+f"&MLSV_YMD={dt.strftime('%Y%m%d')}")
    date_head = response['mealServiceDietInfo'][0]['head']
    #[0]은 list_total_count
    #[1]은 {'RESULT': {'CODE': 'INFO-000', 'MESSAGE': '정상 처리되었습니다.'}}
    date_body = response['mealServiceDietInfo'][1]['row'][0]
    return date_body
    

#호출한 날짜의 급식정보 딕셔너리리턴