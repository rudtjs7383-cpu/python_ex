# ==========================================
# ID / Pw 찾기 모듈
# ==========================================

import random
import members_data


# ==========================================
# 회원 존재 여부 확인
# ==========================================

def isMember(uId):

    return uId in members_data.members


# ==========================================
# EMAIL 확인
# ==========================================

def checkEmail(uId, uMail):

    return members_data.members[uId]['uMail'] == uMail


# ==========================================
# 임시 비밀번호 생성
# ==========================================

def createTempPassword():

    tempPw = random.randint(1000, 9999)

    return str(tempPw)


# ==========================================
# ID 찾기
# ==========================================

def findID():

    print('\n[ ID 찾기 ]')


    while True:

        uMail = input('등록된 EMAIL 입력: ').strip()

        found = False


        for uId, uInfo in members_data.members.items():

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
# Pw 찾기
# ==========================================

def findPassword():

    print('\n[ Pw 찾기 ]')


    # ID 확인
    while True:

        uId = input('Pw를 찾을 ID 입력: ').strip()

        if isMember(uId):

            break

        else:

            print('존재하지 않는 ID입니다.')
            print('다시 입력하세요.\n')


    # EMAIL 확인
    while True:

        uMail = input('등록된 EMAIL 입력: ').strip()

        if checkEmail(uId, uMail):

            break

        else:

            print('EMAIL이 일치하지 않습니다.')
            print('다시 입력하세요.\n')


    # 임시 비밀번호 생성
    tempPw = createTempPassword()


    # 기존 Pw 변경
    members_data.members[uId]['uPw'] = tempPw


    print('\n임시 비밀번호가 생성되었습니다.')
    print(f'{uMail} 로 임시 비밀번호 메일이 발송되었습니다.')


    # 개발 모드 출력
    print(f'[DEV MODE] 임시 비밀번호: {tempPw}')