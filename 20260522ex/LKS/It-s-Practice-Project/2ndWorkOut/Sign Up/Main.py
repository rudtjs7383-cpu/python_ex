from DB import mem_db
from DB import diary_db
from config_dir.dir import config




numChoice = int(input('번호를 선택하세요 >> '))


if numChoice == config.SIGN_UP:
    print('--- 1.sign-up ---')
    
   
    def checkduplicateId(input_id):
       
        if input_id in mem_db.memberdb:
            return True   
        else:
            return False  


    
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
    
   
    mem_db.memberdb[uId] = {
        'uId': uId, 'uPw': uPw, 'uMail': uMail, 'uPhone': uPhone
    }
    
    diary_db.diarydb[uId] = [] 
    print('New member sign-up success!!')
    
   
    if config.DEV_MOD:
        print(f'memberDB: {mem_db.memberdb}')
        print(f'diaryDB: {diary_db.diarydb}')







