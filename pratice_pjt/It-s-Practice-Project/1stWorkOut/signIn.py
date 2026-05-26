
def signIn(members):
    while True:
        print('로그인을 위해 ID 와 PW를 입력하세요.')
        inputId = input('ID를 입력하세요.\nID: ')
        
        for member in members:
            if inputId == member['id']:
                signInCount = 0
                while signInCount < 3:
                    inputPW = input('PW를 입력하세요.\nPW: ')
                    if inputPW == member['pw']:
                        print(f'로그인에 성공하였습니다.\n{member["id"]}님 환영합니다.')
                        return True
                    else:
                        signInCount += 1
                        print(f'로그인 실패: 올바지 않은 PW 입니다.\n남은 시도 횟수 {3 - signInCount}회')
                print('PW 입력 3회 실패로 로그인 기능을 종료합니다.')
                return False
        
        print('올바르지 않은 ID 입니다.\nID를 다시 확인 후 입력하세요.')

