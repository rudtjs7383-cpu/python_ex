# 더미데이터 추가 및 0, 0 까지에서 정의한 menuChoice수정 변수 수정
# 멤버 리스트의 객체가 다음 협업자가 올린 코드와 겹쳐 에러가발생하여 수정

members = {}
    

# 
if selectedMenuNum == '1':                 #임경선
 print('\n--- 회원 가입 메뉴입니다. ---')
 
 
 while True:
     uId= input('사용하실 ID를 입력해주세요: ').strip() 
     if any(members['id'] == uId for members in members):
         print("이미 존재하는 ID입니다. 다시 입력해주세요.")
     else:
         break 
         
 
 uPw = input('사용하실 Pw를 입력해주세요: ').strip()
 
 
 while True:
     uMail = input('Email을 입력해주세요: ').strip()
     if any(members['email'] == uMail for members in members):
         print("이미 등록된 Email입니다. 다시 입력해주세요.")
     else:
         break 
         
 
 while True:
     uPhone = input('휴대전화번호를 입력해주세요: ').strip()
     if any(members['phone'] == uPhone for members in members):
         print("이미 등록된 휴대전화번호입니다. 다시 입력해주세요.")
     else:
         break 
 
 members.append({'id': uId, 'pw': uPw, 'email': uMail, 'phone': uPhone})
 print(f"회원가입이 성공적으로 완료되었습니다! (현재 회원 수: {len(members)}명)")
 print("\n[현재 전체 회원 목록]")
 for member in members:
   print(member)   
