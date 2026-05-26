# 0.:  99번 입력 시 프로그램 종료
# 0.0 : 0번 매뉴 출력

# =========================
# 상수
# =========================
SIGN_UP = 1
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
FIND_ID = 5
FIND_PASSWORD = 6
SYSTEM_SHUTDOWN = 0

EXIT = 7
CANCEL = 8

flag = True


# =========================
# 메뉴 출력
# =========================
def showMenu():

    print('\n' + '=' * 40)
    print('회원 관리 프로그램')
    print('=' * 40)

    print(f'{SIGN_UP}. 회원가입')
    print(f'{SIGN_IN}. 로그인')
    print(f'{PRINT_MY_INFO}. 나의 정보 출력')
    print(f'{PRINT_ALL_MEMBER_INFO}. 모든 회원 정보 출력')
    print(f'{FIND_ID}. id 찾기')
    print(f'{FIND_PASSWORD}. pw 찾기')
    print(f'{SYSTEM_SHUTDOWN}. 종료')

    return int(input('메뉴 선택: '))


# =========================
# 종료 메뉴
# =========================
def exitMenu():

    while True:

        print('\n정말로 종료하시겠습니까?')
        print('7. 종료')
        print('8. 취소')

        numChoice = int(input('번호를 선택하세요>> '))

        if numChoice == EXIT:
            print('프로그램을 종료합니다.')
            return True

        elif numChoice == CANCEL:
            print('메뉴로 돌아갑니다.')
            return False

        else:
            print('잘못된 입력입니다.')