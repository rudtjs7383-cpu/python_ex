# 현재 로그인된 회원의 ID를 저장하는 전역 변수 (초기값은 로그인되지 않은 상태인 None)
signInedMemberId = ''

# setter
def setSignInedMemberId(mId=''):
    global signInedMemberId
    signInedMemberId = mId

# getter
def getSignInedMemberId():
    return signInedMemberId



