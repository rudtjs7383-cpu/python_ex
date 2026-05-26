SIGN_UP = 1
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
FIND_ID = 5
FIND_PASSWORD = 6
SYSTEM_SHUTDOWN = 0

EXIT = 7
CANCEL = 8

DEV_MOD = True


def exitMenu():

    while True:

        print('\n정말로 종료하시겠습니까?')
        print('7. 종료')
        print('8. 취소')

        numChoice = int(input('번호를 선택하세요 >> '))

        # 종료
        if numChoice == EXIT:
            print('프로그램을 종료합니다.')
            return False

        # 취소
        elif numChoice == CANCEL:
            print('메뉴로 돌아갑니다.')
            return True

        # 잘못 입력
        else:
            print('잘못된 입력입니다.')