# ==========================================
# 메인 실행 파일
# ==========================================

import menuExit
import signUp
import signIn
import printMember
import forgotPw


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
# 프로그램 시작
# ==========================================

flag = True


while flag:

    menuExit.showMenu()

    selectedMenuNum = int(input('번호 선택: '))


    # 회원가입
    if selectedMenuNum == SIGN_UP:

        signUp.signUp()


    # 로그인
    elif selectedMenuNum == SIGN_IN:

        signIn.signIn()


    # 특정 회원 정보 출력
    elif selectedMenuNum == PRINT_MY_INFO:

        printMember.printMyInfo()


    # 모든 회원 정보 출력
    elif selectedMenuNum == PRINT_ALL_MEMBER_INFO:

        printMember.printAllMembers()


    # ID 찾기
    elif selectedMenuNum == FIND_ID:

        forgotPw.findID()


    # PW 찾기
    elif selectedMenuNum == FIND_PW:

        forgotPw.findPassword()


    # 프로그램 종료
    elif selectedMenuNum == SYSTEM_EXIT:

        print('\n프로그램 종료')

        flag = False


    # 잘못된 입력
    else:

        print('잘못된 입력입니다.')