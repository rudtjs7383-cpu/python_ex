import datetime
import email.utils
import json
import os
import urllib.parse
import urllib.request

client_id = "PC4EDXNa5QvtIhIBMJ53"
client_secret = "7NhctXVyRI"


# NAVER에서 데이터 가져오는 녀석
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f"[{datetime.datetime.now()}] URL REQUEST SUCCESS!!")

            # 🔥 [수정] .read()는 딱 여기서 단 한 번만 명확하게 호출합니다.
            # 이 순간 raw_data는 'bytes' 데이터가 됩니다.
            raw_data = response.read()

            # 바이트 데이터를 문자열로 디코딩해서 리턴합니다. (뒤에 절대 .read()를 또 붙이면 안 됩니다!)
            return raw_data.decode("utf-8")

    except Exception as e:
        print(f"❌ [getRequestUrl 에러] 네이버 연결 실패: {e}")
        return None


# NAVER에서 데이터 검색하는 녀석
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"

    encText = urllib.parse.quote(srcText)
    parameters = f"?query={encText}&start={start}&display={display}"
    url = base + node + parameters

    responseDecode = getRequestUrl(url)

    if responseDecode is None or responseDecode == "":
        return None
    else:
        return json.loads(responseDecode)


# 데이터 정제하는 녀석
def getPostData(post, jsonResult, cnt):
    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]

    try:
        parsed_date = email.utils.parsedate_to_datetime(post["pubDate"])
        pDate = parsed_date.strftime("%Y-%m-%d %H:%M:%S")
    except:
        pDate = post["pubDate"]

    jsonResult.append(
        {
            "cnt": cnt,
            "title": title,
            "description": description,
            "org_link": org_link,
            "link": link,
            "pDate": pDate,
        }
    )


def main():
    node = "news"
    srcText = input("검색어 입력: ")
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)

    while jsonResponse is not None and jsonResponse.get("display", 0) != 0:
        for post in jsonResponse["items"]:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        next_start = jsonResponse["start"] + jsonResponse["display"]
        if next_start > 1000:
            break
        jsonResponse = getNaverSearch(node, srcText, next_start, 100)

    print(f"▶️ 수집된 데이터 총 개수: {cnt}개")

    # 파일 저장 경로 자동 지정 (파이썬 파일 바로 옆)
    current_folder = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_folder, f"{srcText}_naver_{node}.json")

    if cnt > 0:
        try:
            with open(filename, "w", encoding="utf8") as f:
                jsonFile = json.dumps(
                    jsonResult, indent=4, sort_keys=True, ensure_ascii=False
                )
                f.write(jsonFile)
            print(f"\n🏁 [성공] {srcText}_naver_{node}.json 파일 저장 완료!")
            print(f"📂 파일 위치: {filename}")
        except Exception as e:
            print(f"❌ [파일 저장 에러] 쓰기 실패: {e}")
    else:
        print("❌ 수집된 데이터가 0개여서 파일을 저장하지 않았습니다.")


if __name__ == "__main__":
    main() 