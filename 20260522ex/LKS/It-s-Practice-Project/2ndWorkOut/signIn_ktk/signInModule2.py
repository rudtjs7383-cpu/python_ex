

def signIn(users):
    print('로그인을 위해 id 와 pw를 입력하세요.')
    while True:
       
        inputId = input('id를 입력하세요.\nid: ')
        
        for user in users:
            if user['id'] == inputId:
                signInFail = 0
                while signInFail < 3:
                    inputPw = input('pw를 입력하세요.\npw: ')
                    if inputPw == user['pw']:
                        print(f'로그인에 성공하였습니다.\n{user["id"]}님 환영합니다.')
                        return True
                    else:
                        signInFail += 1
                        print(f'로그인 실패: 올바르지 않은 pw 입니다.\n남은 시도 횟수 {3 - signInFail}회')
                print('pw 입력 3회 실패로 로그인 기능을 종료합니다.')
                return False
        
        print('올바르지 않은 id 입니다.\nid를 다시 확인 후 입력하세요.')

