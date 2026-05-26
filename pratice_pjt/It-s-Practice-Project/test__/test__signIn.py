# ==========================================
# 로그인 모듈
# signIn.py
# ==========================================

import members_data


def signIn():

    print('\n[ 로그인 ]')


    # ==========================================
    # ID 확인
    # ==========================================

    while True:

        uId = input('ID 입력: ').strip()


        # 존재하는 ID라면 반복 종료
        if uId in members_data.members:

            break


        # 존재하지 않는 ID
        else:

            print('존재하지 않는 ID입니다.')
            print('다시 입력하세요.\n')


    # ==========================================
    # PW 확인
    # ==========================================

    signInCount = 0


    while signInCount < 3:

        uPw = input('PW 입력: ').strip()


        # 로그인 성공
        if members_data.members[uId]['uPw'] == uPw:

            print(f'\n{uId}님 로그인 성공')

            return True


        # 로그인 실패
        else:

            signInCount += 1

            print(f'PW 불일치 ({3 - signInCount}회 남음)')


    print('로그인 3회 실패')

    return False