import random

from member import memberDumy
from db import memberDB
from config_dir.dir import config



if config.DEV_MOD:

    memberDumy.dummyInit()

    print(memberDB.memberDB)



def isMember(uId):

    return uId in memberDB.memberDB


def checkEmail(uId, uMail):

    return memberDB.memberDB[uId]['uMail'] == uMail



def createTempPassword():

    tempPw = random.randint(1000, 9999)

    return str(tempPw)



def findID():

    print('\n[ 아이디 찾기 ]')

    while True:

        uMail = input('등록된 EMAIL 입력: ')

        found = False

        for uId, uInfo in memberDB.memberDB.items():

            if uInfo['uMail'] == uMail:

                print(f'\n{uMail} 로 ID 메일이 발송되었습니다.')

                found = True

                break

        if found:

            break

        else:

            print('등록되지 않은 EMAIL입니다.')
            print('다시 입력하세요.\n')



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

    memberDB.memberDB[uId]['uPw'] = tempPw

    print('\n임시 비밀번호가 생성되었습니다.')
    print(f'{uMail} 로 임시 비밀번호 메일이 발송되었습니다.')

    if config.DEV_MOD:

        print(f'[DEV MODE] 임시 비밀번호: {tempPw}')



if __name__ == '__main__':

    flag = True

    while flag:

        print('\n메뉴')
        print('1. 아이디 찾기')
        print('2. 비밀번호 찾기')
        print('99. 종료')

        menuNum = int(input('번호 선택: '))

        if menuNum == 1:

            findID()

        elif menuNum == 2:

            findPassword()

        elif menuNum == 99:

            print('프로그램 종료')

            flag = False

        else:

            print('잘못 입력했습니다.')