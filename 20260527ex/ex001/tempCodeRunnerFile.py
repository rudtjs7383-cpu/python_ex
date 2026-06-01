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
