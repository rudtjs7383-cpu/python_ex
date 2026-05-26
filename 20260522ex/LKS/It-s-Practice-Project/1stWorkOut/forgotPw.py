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