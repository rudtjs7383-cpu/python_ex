# 더미데이터 추가 및 0, 0 까지에서 정의한 menuChoice수정 변수 수정
# 멤버 리스트의 객체가 다음 협업자가 올린 코드와 겹쳐 에러가발생하여 수정
import random                                           #상수 추가 및 함수 추가
import string


SIGN_UP = 1
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
FIND_ID = 5
FIND_PW = 6
SYSTEM_SHUTDOWN = 0  
DEV_MOD = True




members = {}
flag = True










def signUp():
    while True:
     print('\n--- 회원 가입 메뉴입니다. ---')
    
    
     while True:
        uId = input('사용하실 ID를 입력해주세요: ').strip() 
        if uId in members:
            print("이미 존재하는 ID입니다. 다시 입력해주세요.")
        else:
            break 
            
     uPw = input('사용하실 Pw를 입력해주세요: ').strip()


     while True:
        uMail = input('Email을 입력해주세요: ').strip()
        if any(info['email'] == uMail for info in members.values()):
            print("이미 등록된 Email입니다. 다시 입력해주세요.")
        else:
            break 
            
    
     while True:
        uPhone = input('휴대전화번호를 입력해주세요: ').strip()
        if any(info['phone'] == uPhone for info in members.values()):
            print("이미 등록된 휴대전화번호입니다. 다시 입력해주세요.")
        else:
            break 


    
     members[uId] = {'pw': uPw, 'email': uMail, 'phone': uPhone}
    
     print(f"\n회원가입이 성공적으로 완료되었습니다! (현재 회원 수: {len(members)}명)")
     print("[현재 전체 회원 목록]")
     for m_id, m_info in members.items():
        print(f"ID: {m_id}, 정보: {m_info}")


  
   




while True:
    print('\n메뉴')
    print('1. 회원가입')
    print('2. 로그인')
    print('3. 특정 회원 정보 출력')
    print('4. 모든 회원 정보 출력')
    print('5. id 찾기')
    print('6. pw 찾기')
    print('0. 종료')


    try:
        selectedMenuNum = int(input('번호 선택: '))
    except ValueError:
        print('숫자만 입력 가능합니다. 다시 선택해주세요.')
        continue
    if selectedMenuNum == SIGN_UP:
        signUp()  

















































































