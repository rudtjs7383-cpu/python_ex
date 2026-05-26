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