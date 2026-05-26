from DB import mem_db
from DB import diary_db
from config_dir.dir import config


numChoice = int(input('번호를 선택하세요 >> '))


if numChoice == config.SIGN_UP:
    print('--- 1.sign-up ---')

    uId = input('사용하실 ID를 입력하세요')
    uPw = input('사용하실 PW를 입력하세요')
    uMail = input('사용하실 Email을 입력하세요')
    uPhone = input('사용하실 번호를 입력하세요')
    
    
    
    

    mem_db.memberdb[uId] = {
        'uId': uId, 'uPw': uPw, 'uMail': uMail, 'uPhone': uPhone
    }
    
    diary_db.diarydb[uId] = [] 
    print('New member sign-up success!!')
    if config.DEV_MOD:
        print(f'memberDB: {mem_db.memberDB}')
        print(f'diaryDB: {diary_db.diaryDB}')















