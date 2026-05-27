import datetime
import json
import urllib.parse
import urllib.request
from flask import Flask, render_template, request

app = Flask(__name__)

client_id = "PC4EDXNa5QvtIhIBMJ53"
client_secret = "7NhctXVyRI"


# NAVER API 요청 함수
def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print(f"[{datetime.datetime.now()}] Request Success")
            return response.read().decode("utf-8")
    except Exception as e:
        print(e)
        return None


# NAVER 뉴스 검색
def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = f"/{node}.json"
    parameters = (
        f"?query={urllib.parse.quote(srcText)}&start={start}&display={display}"
    )
    url = base + node + parameters

    responseDecode = getRequestUrl(url)
    if responseDecode is None:
        return None
    else:
        return json.loads(responseDecode)


# 뉴스 데이터 정리
def getPostData(post, jsonResult, cnt):
    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]

    try:
        pDate = datetime.datetime.strptime(
            post["pubDate"], "%a, %d %b %Y %H:%M:%S +0900"
        )
        pDate = pDate.strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
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


@app.route("/", methods=["GET", "POST"])
def index():
    # HTML에 넘겨줄 변수들을 미리 초기화합니다.
    news_list = []
    srcText = ""
    cnt = 0

    if request.method == "POST":
        # ⚠️ [수정 포인트 1] 
        # HTML의 input 태그 name이 "search_word"이므로, 여기서도 "search_word"로 가져와야 합니다.
        # 안전하게 .get()을 사용하여 BadRequestKeyError를 원천 차단합니다.
        srcText = request.form.get("search_word", "")

        node = "news"
        jsonResult = []

        if srcText:
            jsonResponse = getNaverSearch(node, srcText, 1, 10)

            while jsonResponse is not None and jsonResponse["display"] != 0:
                for post in jsonResponse["items"]:
                    cnt += 1
                    getPostData(post, jsonResult, cnt)
                break

            # JSON 파일 저장
            with open(
                f"{srcText}_naver_news.json", "w", encoding="utf-8"
            ) as f:
                jsonFile = json.dumps(
                    jsonResult, indent=4, ensure_ascii=False
                )
                f.write(jsonFile)

            news_list = jsonResult

    # ⚠️ [수정 포인트 2]
    # 질문자님의 index.html 템플릿 문법 구조와 완벽히 매칭되도록 변수명을 맞춰서 보냅니다.
    # HTML에서 {{ search_word }}, {{ total_cnt }}, {% for item in results %}를 쓰고 있습니다.
    return render_template(
        "index.html", results=news_list, search_word=srcText, total_cnt=cnt
    )


if __name__ == "__main__":
    app.run(debug=True)