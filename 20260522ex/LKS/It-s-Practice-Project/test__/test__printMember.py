# ==========================================
# 회원 정보 출력 모듈
# ==========================================

import members_data


# ==========================================
# 특정 회원 정보 출력
# ==========================================

def printMyInfo():

    print('\n[ 특정 회원 정보 출력 ]')

    uId = input('ID 입력: ').strip()
    uPw = input('PW 입력: ').strip()


    if uId in members_data.members:

        if members_data.members[uId]['uPw'] == uPw:

            print('\n로그인 성공')

            print('-' * 40)

            print(f'회원ID: {uId}')


            for key, value in members_data.members[uId].items():

                if key == 'uPw':

                    print(f'{key}: {"*" * len(value)}')

                else:

                    print(f'{key}: {value}')


            print('-' * 40)

        else:

            print('PW가 일치하지 않습니다.')

    else:

        print('존재하지 않는 ID입니다.')



# ==========================================
# 모든 회원 정보 출력
# ==========================================

def printAllMembers():

    print('\n[ 전체 회원 정보 출력 ]')


    if len(members_data.members) == 0:

        print('가입된 회원이 없습니다.')
        return


    for uId, uInfo in members_data.members.items():

        print('-' * 40)

        print(f'회원ID: {uId}')


        for key, value in uInfo.items():

            if key == 'uPw':

                print(f'{key}: {"*" * len(value)}')

            else:

                print(f'{key}: {value}')


        print('-' * 40)