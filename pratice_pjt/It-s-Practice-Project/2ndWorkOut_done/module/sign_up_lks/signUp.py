from db import memberDB
from db import diaryDB
from config_dir.dir import config



'''
numChoice = int(input('번호를 선택하세요 >> '))


if numChoice == config.SIGN_UP:
    print('--- 1.sign-up ---')
'''
# 위 부분은 main에서 다룰 것

   
def checkduplicateId(input_id):
    
    if input_id in memberDB.memberDB:
        return True   
    else:
        return False  


def signUp():

    print('--- 1.sign-up ---')

    while True:
        uId = input('사용하실 ID를 입력하세요: ')
        
        if checkduplicateId(uId): 
            print(" 이미 존재하는 ID입니다. 다른 ID를 입력해주세요.")
            continue  

        else:
            print(" 사용 가능한 ID입니다.")
            break  



    uPw = input('사용하실 PW를 입력하세요: ')
    uMail = input('사용하실 Email을 입력하세요: ')
    uPhone = input('사용하실 번호를 입력하세요: ')
   
    memberDB.memberDB[uId] = {
        'uId': uId, 'uPw': uPw, 'uMail': uMail, 'uPhone': uPhone
    }
        
    diaryDB.diaryDB[uId] = []
    print('New member sign-up success!!')


    if config.DEV_MOD:
        print(f'memberDB: {memberDB.memberDB}')
        print(f'diaryDB: {diaryDB.diaryDB}')


'''
from db import memberDB
from db import diaryDB
from config_dir.dir import config



def checkduplicateId(input_id):

    if input_id in memberDB.memberDB:

        return True

    else:

        return False



def signUp():

    print('--- 1.sign-up ---')



    # ==========================================
    # ID 입력
    # ==========================================

    while True:

        uId = input('사용하실 ID를 입력하세요: ')

        if checkduplicateId(uId):

            print('이미 존재하는 ID입니다.')

        else:

            print('사용 가능한 ID입니다.')

            break



    # ==========================================
    # 회원 정보 입력
    # ==========================================

    uPw = input('사용하실 PW를 입력하세요: ')
    uMail = input('사용하실 Email을 입력하세요: ')
    uPhone = input('사용하실 번호를 입력하세요: ')



    # ==========================================
    # 회원 정보 저장
    # ==========================================

    memberDB.memberDB[uId] = {

        'uId': uId,
        'uPw': uPw,
        'uMail': uMail,
        'uPhone': uPhone

    }



    # ==========================================
    # diary 생성
    # ==========================================

    diaryDB.diaryDB[uId] = []



    print('New member sign-up success!!')



    if config.DEV_MOD:

        print(f'memberDB: {memberDB.memberDB}')
        print(f'diaryDB: {diaryDB.diaryDB}')

'''