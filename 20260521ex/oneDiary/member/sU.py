
def check_duplicate_id(input_id):
    """
    [함수 1] 사용자가 입력한 ID가 이미 DB에 존재하는지 중복 체크를 합니다.
    """
    
    if input_id in mem_db.memberdb:
        return True   
    else:
        return False  


def save_member_data(uId, uPw, uMail, uPhone):
    """
    [함수 2] 입력받은 4가지 정보를 딕셔너리로 묶어서 DB에 최종 저장합니다.
    """
    mem_db.memberdb[uId] = {
        'uId': uId, 
        'uPw': uPw, 
        'uMail': uMail, 
        'uPhone': uPhone
    }




from DB import mem_db
from DB import diary_db
from config_dir.dir import config
from member import signup  # 👈 이제 이 문장이 에러 없이 작동합니다!

numChoice = int(input('번호를 선택하세요 >> '))

if numChoice == config.SIGN_UP:
    print('--- 1.sign-up ---')

   
    while True:
        uId = input('사용하실 ID를 입력하세요: ')
        if sU.check_duplicate_id(uId):
            print("❌ 이미 존재하는 아이디입니다.")
            continue
        else:
            print("✅ 사용 가능한 아이디입니다.")
            break

    uPw = input('사용하실 PW를 입력하세요: ')
    uMail = input('사용하실 Email을 입력하세요: ')
    uPhone = input('사용하실 번호를 입력하세요: ')
    
    
    sU.save_member_data(uId, uPw, uMail, uPhone)
    
    diary_db.diarydb[uId] = [] 
    print('New member sign-up success!!')














