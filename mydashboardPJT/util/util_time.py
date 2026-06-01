# util/util_time.py 파일 내용 예시
from datetime import datetime

def getcurrentDateTime():  # member_service.py에서 부르는 이름과 토씨 하나 안 틀리게 수정
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')