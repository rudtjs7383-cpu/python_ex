# TOY 프로젝트 진행

'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴: 1.회원가입   2.로그인   3.특정 회원 정보 출력   
4.모든 회원 정보 출력   99.종료
사용자가 :
'1.회원가입'을 선택하면 회원ID, 회원PW, 회원Email, 회원Phone 
정보를 입력받아 회원가입 진행한다.
'2.로그인'을 선택하면 회원ID, 회원PW를 입력받아 로그인 '성공' 
또는 '실패'를 출력한다.
'3.특정 회원 정보 출력을 선택하면 회원ID와 회원PW를 입력받아 
일치하는 회원 정보를 모두 출력한다.
'4.모든 회원 정보 출력'를 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
'99.종료'를 선택하면 프로그램 종료 시킨다.
'''

# ---------------------------------------------------------------------------------------------
# 개선안 
# ---------------------------------------------------------------------------------------------

import random


# ==========================================
# 상수(Constant)
# ==========================================

SIGN_UP               = 1
SIGN_IN               = 2
PRINT_MY_INFO         = 3
FIND_ID               = 4
FIND_PASSWORD         = 5
PRINT_ALL_MEMBER_INFO = 6
SYSTEM_SHUTDOWN       = 99


# ==========================================
# 개발 모드
# ==========================================

DEV_MODE = True


# ==========================================
# 회원 정보 저장 딕셔너리
# ==========================================

members = {}


# ==========================================
# 테스트 계정 생성
# ==========================================

if DEV_MODE:

    members['gildong'] = {

        'uPw': '1234',
        'uMail': 'gildong@gmail.com',
        'uPhone': '010-1234-5678'

    }


# ==========================================
# 메뉴 출력 함수
# ==========================================

def showMenu():

    print('\n' + '=' * 40)
    print('회원 관리 프로그램')
    print('=' * 40)

    print(f'{SIGN_UP}. 회원가입')
    print(f'{SIGN_IN}. 로그인')
    print(f'{PRINT_MY_INFO}. 나의 정보 출력')
    print(f'{FIND_ID}. 아이디 찾기')
    print(f'{FIND_PASSWORD}. 비밀번호 찾기')
    print(f'{PRINT_ALL_MEMBER_INFO}. 모든 회원 정보 출력')
    print(f'{SYSTEM_SHUTDOWN}. 종료')


# ==========================================
# 회원 존재 여부 확인
# ==========================================

def isMember(uId):

    return uId in members


# ==========================================
# 비밀번호 확인
# ==========================================

def checkPassword(uId, uPw):

    return members[uId]['uPw'] == uPw


# ==========================================
# 이메일 확인
# ==========================================

def checkEmail(uId, uMail):

    return members[uId]['uMail'] == uMail


# ==========================================
# 임시 비밀번호 생성
# 숫자 4자리
# ==========================================

def createTempPassword():

    tempPw = random.randint(1000, 9999)

    return str(tempPw)


# ==========================================
# 회원 정보 출력
# ==========================================

def printMemberData(uId):

    uInfo = members[uId]

    print('-' * 40)

    print(f'회원ID: {uId}')

    for key, value in uInfo.items():

        print(f'{key}: {value}')

    print('-' * 40)


# ==========================================
# 회원가입
# ==========================================

def signUp():

    print('\n[ 회원가입 ]')

    uId = input('회원 ID 입력: ')
    uPw = input('회원 PW 입력: ')
    uMail = input('회원 EMAIL 입력: ')
    uPhone = input('회원 PHONE 입력: ')

    if isMember(uId):

        print('이미 존재하는 회원 ID입니다.')
        return

    members[uId] = {

        'uPw': uPw,
        'uMail': uMail,
        'uPhone': uPhone

    }

    print('회원가입 완료')


# ==========================================
# 로그인
# ==========================================

def signIn():

    print('\n[ 로그인 ]')

    uId = input('회원 ID 입력: ')
    uPw = input('회원 PW 입력: ')

    if not isMember(uId):

        print('존재하지 않는 회원입니다.')
        return

    if checkPassword(uId, uPw):

        print('로그인 성공')

    else:

        print('비밀번호가 일치하지 않습니다.')


# ==========================================
# 나의 정보 출력
# ==========================================

def printMyInfo():

    print('\n[ 나의 정보 출력 ]')

    uId = input('회원 ID 입력: ')
    uPw = input('회원 PW 입력: ')

    if not isMember(uId):

        print('존재하지 않는 회원입니다.')
        return

    if checkPassword(uId, uPw):

        print('\n로그인 성공')

        printMemberData(uId)

    else:

        print('비밀번호가 일치하지 않습니다.')


# ==========================================
# 아이디 찾기
# ==========================================

def findID():

    print('\n[ 아이디 찾기 ]')

    while True:

        uMail = input('등록된 EMAIL 입력: ')

        found = False

        for uId, uInfo in members.items():

            if uInfo['uMail'] == uMail:

                print(f'\n{uMail} 로 ID 메일이 발송되었습니다.')

                found = True

                break

        if found:

            break

        else:

            print('등록되지 않은 EMAIL입니다.')
            print('다시 입력하세요.\n')


# ==========================================
# 비밀번호 찾기
# ==========================================

def findPassword():

    print('\n[ 비밀번호 찾기 ]')

    while True:

        uId = input('PW를 찾을 회원 ID 입력: ')

        if isMember(uId):

            break

        else:

            print('존재하지 않는 ID입니다.')
            print('다시 입력하세요.\n')

    while True:

        uMail = input('등록된 EMAIL 입력: ')

        if checkEmail(uId, uMail):

            break

        else:

            print('EMAIL이 일치하지 않습니다.')
            print('다시 입력하세요.\n')

    tempPw = createTempPassword()

    members[uId]['uPw'] = tempPw

    print('\n임시 비밀번호가 생성되었습니다.')
    print(f'{uMail} 로 임시 비밀번호 메일이 발송되었습니다.')

    if DEV_MODE:

        print(f'[DEV MODE] 임시 비밀번호: {tempPw}')


# ==========================================
# 전체 회원 정보 출력
# ==========================================

def printAllMemberInfo():

    print('\n[ 전체 회원 정보 출력 ]')

    if len(members) == 0:

        print('가입된 회원이 없습니다.')
        return

    for uId in members:

        printMemberData(uId)


# ==========================================
# 프로그램 시작
# ==========================================

flag = True

while flag:

    showMenu()

    selectedMenuNum = int(input('메뉴 선택: '))

    if selectedMenuNum == SIGN_UP:

        signUp()

    elif selectedMenuNum == SIGN_IN:

        signIn()

    elif selectedMenuNum == PRINT_MY_INFO:

        printMyInfo()

    elif selectedMenuNum == FIND_ID:

        findID()

    elif selectedMenuNum == FIND_PASSWORD:

        findPassword()

    elif selectedMenuNum == PRINT_ALL_MEMBER_INFO:

        printAllMemberInfo()

    elif selectedMenuNum == SYSTEM_SHUTDOWN:

        flag = False

        print('프로그램 종료')

    else:

        print('잘못 입력했습니다.')