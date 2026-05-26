import sys


users = [
    {'id':'gildong','pw':'passwords','email':'abc1234@gmail.com','phone':'010-1234-5678'},
    {'id':'seri02','pw':'123422','email':'xxx1234@gmail.com','phone':'010-1234-5555'},
    {'id':'chanho03','pw':'abc1234','email':'top1234@gmail.com','phone':'010-1234-6666'},
    {'id':'meow04','pw':'cat1234','email':'googoo@gmail.com','phone':'010-1234-7777'}
]
loginFailAcount = 0


while True:
    print('1. 회원가입\n2. 로그인\n3. 회원정보 출력\n4. 모든회원정보 출력\n5. ID찾기\n6. PW찾기\n0.종료')


    menu = input('메뉴를 입력하세요 :').strip()


    if menu == '0':
        print('사용자가 종료를 눌렀습니다.')
        sys.exit()


    elif menu == '1':
        print('\n--- 회원 가입 메뉴입니다. ---')


        while True:
            newId = input('사용하실 ID를 입력해주세요: ').strip()
            if any(user['id'] == newId for user in users):
                print("이미 존재하는 ID입니다. 다시 입력해주세요.")
            else:
                break


        newPw = input('사용하실 Pw를 입력해주세요: ').strip()


        while True:
            newMail = input('Email을 입력해주세요: ').strip()
            if any(user['email'] == newMail for user in users):
                print("이미 등록된 Email입니다. 다시 입력해주세요.")
            else:
                break


        while True:
            newPhone = input('휴대전화번호를 입력해주세요: ').strip()
            if any(user['phone'] == newPhone for user in users):
                print("이미 등록된 휴대전화번호입니다. 다시 입력해주세요.")
            else:
                break



        users.append({'id': newId, 'pw': newPw, 'email': newMail, 'phone': newPhone})
        print(f"회원가입이 성공적으로 완료되었습니다! (현재 회원 수: {len(users)}명)")