import urllib.request
import datetime
import json

SERVICE_KEY = 'dd361afaa3348a49d20a418e8284468e2251747842e76dc2492eb3334930a6ea'

def getRequestURL(url):
    req = urllib.request.Request(url)

    try:
        res = urllib.request.urlopen(req)
        if res.getcode() == 200:
            print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION SUCCESS!!')
            return res.read().decode('utf-8')
    except Exception as e:
        print(f'[{datetime.datetime.now()}]REQUEST COMMUNICATION FAIL!!')
        print(f'e: {e}')
        return None

def getTourismStatesItem(yyyymm, nat_cd, ed_cd):
    serviceURL = 'http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList'

    parameters = "?"
    parameters += "_type=json&"
    parameters += "serviceKey=" + SERVICE_KEY + '&'
    parameters += "YM=" + yyyymm + '&'
    parameters += "ED_CD=" + ed_cd + '&'
    parameters += "NAT_CD=" + nat_cd

    url = serviceURL + parameters
    res = getRequestURL(url)            # None or not None
    if res == None:
        return None
    else:
        return json.loads(res)
        # json.loads() 는 JSON 형식의 문자열(str)을 파이썬 애플리케이션에서 쉽게 사용할 수 있도록 변환함.
        # JSON 형식의 문자열(str) ----> dic 객체

def getTourismStatesService(nat_cd, ed_cd, nStartYear, nEndYear):

    jsonResult = []
    result = []
    natName = ''
    isDataEnd = 0
    dataEnd = f'{str(nEndYear)}{str(12)}'       # 202012

    # 2025 ~ 2026   :   1 ~ 12, 1 ~ 5
    for year in range(nStartYear, nEndYear + 1):        # 년
        for month in range(1, 13):                      # 월
            if isDataEnd == 1:                          
                break


            yyyymm = f'{str(year)}{str(month):0>2}'                   # 2020 ~ 2021 : 202003(o) 20203 (x)
            jsonData = getTourismStatesItem(yyyymm, nat_cd, ed_cd)
            if jsonData['response']['header']['resultMsg'] == 'OK':
                
                # 데이터 끝 확인
                if jsonData['response']['body']['items'] == '':
                    isDataEnd = 1   # 데이터 끝 확인용 flag 변수
                    dataEnd = f'{year}{str(month-1):0>2}'
                    print('DATA END!!')
                    break

                # JSON 데이터 확인
                natName = jsonData['response']['body']['items']['item']['natKorNm']
                # 중  국 > 중국
                natName = natName.replace(' ', '')
                num = jsonData['response']['body']['items']['item']['num']  # 방문자 수 > 481681
                ed = jsonData['response']['body']['items']['item']['ed']    # "방한외래관광객"
                print(f'[{natName}][{num}][{ed}]')

                jsonResult.append({
                    'nat_name': natName,
                    'nat_cd': nat_cd,
                    'yyyymm': yyyymm,
                    'visit_cnt': num,
                })

    return (jsonResult, natName, ed, dataEnd)
                
def main():

    jsonResult = []
    natName = ''

    print('---------------------------------------')
    print('-----국내 입국한 외국인 통계 데이터----')
    print('---------------------------------------')

    nat_cd = input('국가 코드 입력[중국(112), 일본(130), 미국(275))]: ')
    nStartYear = int(input('데이터 수집 시작 년도: '))
    nEndYear = int(input('데이터 수집 끝 년도: '))
    ed_cd = 'E' # E: 입국   D: 출국

    jsonResult, natName, ed, dataEnd = getTourismStatesService(nat_cd, ed_cd, nStartYear, nEndYear)
    # print(f'jsonResult: {jsonResult}')
    # print(f'natName: {natName}')
    # print(f'ed: {ed}')
    # print(f'dataEnd: {dataEnd}')

    if natName == '':
        print('데이터 수집 오류!! 서버 담당자한테 문의 하세요.!!!')
    else:
        print('데이터 수집 성공!!')
        with open(f'./{natName}_{ed}_{nStartYear}{dataEnd}.json', 'w', encoding='utf-8') as f:
            jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
            f.write(jsonFile)

if __name__ == '__main__':
    main()