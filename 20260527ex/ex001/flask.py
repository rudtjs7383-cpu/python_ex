import datetime
import email.utils
import json
import os
import urllib.parse
import urllib.request
from flask import Flask, render_template, request

app = Flask(__name__)

# 네이버 API 키 설정
client_id = "PC4EDXNa5QvtIhIBMJ53"
client_secret = "7NhctXVyRI"


# NAVER에서 데이터 가져오는 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f"[{datetime.datetime.now()}] URL REQUEST SUCCESS!!")
            raw_data = response.read()
            return raw_data.decode("utf-8")
    except Exception as e:
        print(f"❌ [getRequestUrl 에러] 네이버 연결 실패: {e}")
        return None


# NAVER에서 데이터 검색하는 함수
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


# 데이터 정제하는 함수
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


# 메인 홈 페이지 (검색창 보여주기 + 검색 결과 출력하기)
@app.route("/", methods=["GET", "POST"])
def index():
    jsonResult = []
    srcText = ""
    cnt = 0

    # 사용자가 웹사이트에서 검색 버튼을 눌렀을 때 (POST 방식)
    if request.method == "POST":
        srcText = request.form.get("search_word", "")
        node = "news"

        if srcText:
            jsonResponse = getNaverSearch(node, srcText, 1, 100)

            while jsonResponse is not None and jsonResponse.get("display", 0) != 0:
                for post in jsonResponse["items"]:
                    cnt += 1
                    getPostData(post, jsonResult, cnt)

                next_start = jsonResponse["start"] + jsonResponse["display"]
                if next_start > 1000:
                    break
                jsonResponse = getNaverSearch(node, srcText, next_start, 100)

            # [기존 기능 유지] 백엔드 콘솔 출력 및 JSON 파일로도 저장해 두기
            print(f"▶️ 수집된 데이터 총 개수: {cnt}개")
            if cnt > 0:
                current_folder = os.path.dirname(os.path.abspath(__file__))
                filename = os.path.join(
                    current_folder, f"{srcText}_naver_{node}.json"
                )
                with open(filename, "w", encoding="utf8") as f:
                    json.dump(jsonResult, f, indent=4, ensure_ascii=False)
                print(f"📂 파일 저장 완료: {filename}")

    # 결과를 index.html 파일로 보내서 화면에 그려줍니다.
    return render_template(
        "index.html", results=jsonResult, search_word=srcText, total_cnt=cnt
    )


if __name__ == "__main__":
    app.run(debug=True)