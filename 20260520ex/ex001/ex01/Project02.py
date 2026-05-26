#1번 팀프로젝트 시나리오

'''
'0.' 메뉴창을 하단과 같이 생성한다.
메뉴: 1 회원가입 2. 로그인 3. 특정 회원 정보 출력 4. 모든 회원 정보 출력 5. Id 찾기 6. Pw 찾기 0. 종료
'5' Id 찾기를 누를시 등록된 이메일로 메일이 발송되었습니다.
ex) 'abcd1234@gmail.com'로 메일이 발송되었습니다.
'6' Pw 찾기를 누를시 사용하던 Id를 입력 하고 등록된 이메일을 입력하면 메일로 임시 Pw 발급
ex) Pw를 찾을 Id를 입력하세요.
등록된 Email을 입력하세요.
'abcd1234@gmail.com'로 임시Pw가 발송되었습니다.(텍스트만 발송)

'1.(나) '회원가입'을 선택하면 회원 ID, PW ,Email, Phone 정보를 입력받아 가입을 진행함.
'1-1' (나) Id, Email, Phone 정보가 중복되는 경우 다음으로 넘어가지 않고 해당 항목을 다시 입력하도록 함
        ex) 이메일 입력하였는데 이메일이 중복될시 이메일을 다시입력하도록함

'2.'     '로그인'을 선택하면 ID, PW 를 입력바아 로그인 성공, 실패를 출력함 3회 실패시 프로그램 종료
'2-1'     로그인 pw 틀릴시 메인으로 돌아오는것이 아닌 id, pw 를 다시입력할수있도록한다.

'3.     '특정 회원 정보 출력'을 선택하면 회원 ID,PW 를 입력받아 일치하는 회원 정보를 모두 출력

'4.     '모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.

'5'     Id 찾기를 누를시 등록된 이메일로 메일이 발송되었습니다.
        ex) 'abcd1234@gmail.com'로 메일이 발송되었습니다.

'6'   Pw 찾기를 누를시 사용하던 Id를 입력 하고 등록된 이메일을 입력하면 메일로 임시 Pw 발급
        ex) Pw를 찾을 Id를 입력하세요.
            등록된 Email을 입력하세요.
            'abcd1234@gmail.com'로 임시Pw가 발송되었습니다.(텍스트만 발송)

'0.     '종료'를 선택하면 프로그램을 종료시킨다.






'''
import sys

users = [
    {'id':'gildong','pw':'passwords','email':'abc1234@gmail.com','phone':'010-1234-5678'},
    {'id':'seri02','pw':'123422','email':'xxx1234@gmail.com','phone':'010-1234-5555'},
    {'id':'chanho03','pw':'abc1234','email':'top1234@gmail.com','phone':'010-1234-6666'}, 
    {'id':'meow04','pw':'cat1234','email':'gooogooo@gmail.com','phone':'010-1234-7777'} 
]
loginFailAcount = 0

while True:
    print('1. 회원가입\n2. 로그인\n3. 회원정보 출력\n4. 모든회원정보 출력\n5. ID찾기\n6. PW찾기\n0. 종료')
    
    
    menu = input('메뉴를 입력하세요 :').strip()

    if menu == '0':
        print('사용자가 종료를 눌렀습니다.')
        sys.exit()

        #elif menu == '1':                 #임경선
        # print('\n--- 회원 가입 메뉴입니다. ---')
        # 
        # 
        # while True:
            # newId = input('사용하실 ID를 입력해주세요: ').strip() 
            # if any(user['id'] == newId for user in users):
                # print("이미 존재하는 ID입니다. 다시 입력해주세요.")
            # else:
                # break 
                # 
        # 
        # newPw = input('사용하실 Pw를 입력해주세요: ').strip()
        # 
        # 
        # while True:
            # newMail = input('Email을 입력해주세요: ').strip()
            # if any(user['email'] == newMail for user in users):
                # print("이미 등록된 Email입니다. 다시 입력해주세요.")
            # else:
                # break 
                # 
        # 
        # while True:
            # newPhone = input('휴대전화번호를 입력해주세요: ').strip()
            # if any(user['phone'] == newPhone for user in users):
                # print("이미 등록된 휴대전화번호입니다. 다시 입력해주세요.")
            # else:
                # break 

        # 
        # users.append({'id': newId, 'pw': newPw, 'email': newMail, 'phone': newPhone})
        # print(f"회원가입이 성공적으로 완료되었습니다! (현재 회원 수: {len(users)}명)")

































