# ==========================================
# 메뉴 출력 모듈
# menuExit.py
# ==========================================


# ==========================================
# 메뉴 상수
# ==========================================

SIGN_UP = 1
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
FIND_ID = 5
FIND_PW = 6
SYSTEM_EXIT = 0


# ==========================================
# 메뉴 출력 함수
# ==========================================

def showMenu():

    print('\n========== 메뉴 ==========')

    print(f'{SIGN_UP}. 회원가입')
    print(f'{SIGN_IN}. 로그인')
    print(f'{PRINT_MY_INFO}. 특정 회원 정보 출력')
    print(f'{PRINT_ALL_MEMBER_INFO}. 모든 회원 정보 출력')
    print(f'{FIND_ID}. ID 찾기')
    print(f'{FIND_PW}. PW 찾기')
    print(f'{SYSTEM_EXIT}. 종료')

    print('=' * 26)