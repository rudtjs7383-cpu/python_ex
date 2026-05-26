# ==========================================
# 회원가입 모듈
# ==========================================

import members_data


def signUp():

    print('\n[ 회원가입 ]')


    # ID 검사
    while True:

        uId = input('사용할 ID 입력: ').strip()

        if uId == '':

            print('ID를 입력하세요.')

        elif uId in members_data.members:

            print('이미 존재하는 ID입니다.')

        elif len(uId) < 4:

            print('ID는 최소 4자리 이상이어야 합니다.')

        else:

            break


    # PW 검사
    while True:

        uPw = input('사용할 PW 입력: ').strip()

        if len(uPw) < 4:

            print('PW는 최소 4자리 이상이어야 합니다.')

        else:

            break


    # EMAIL 검사
    while True:

        uMail = input('EMAIL 입력: ').strip()

        duplicated = False

        for uInfo in members_data.members.values():

            if uInfo['uMail'] == uMail:

                duplicated = True
                break

        if '@' not in uMail:

            print('올바른 EMAIL 형식이 아닙니다.')

        elif duplicated:

            print('이미 등록된 EMAIL입니다.')

        else:

            break


    # PHONE 검사
    while True:

        uPhone = input('PHONE 입력: ').strip()

        duplicated = False

        for uInfo in members_data.members.values():

            if uInfo['uPhone'] == uPhone:

                duplicated = True
                break

        if duplicated:

            print('이미 등록된 PHONE 번호입니다.')

        else:

            break


    # 회원 저장
    members_data.members[uId] = {

        'uPw': uPw,
        'uMail': uMail,
        'uPhone': uPhone

    }

    print('\n회원가입 완료')