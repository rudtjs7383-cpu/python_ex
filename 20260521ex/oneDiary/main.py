from config_dir.dir import config
from member import session
from DB import member_db
from DB import diary_db
from member import member_dumy
import copy


if config.DEV_MOD:
    member_dumy.Dumyinit()
    print(f'memberDB: {member_db.memberDB}')
    print(f'diaryDB: {diary_db.diaryDB}')

flag = True

while flag:
    menuNum = 0 
    
    
    if session.signInedMemberId == '':
        userInput = input('\n1.sign-up    2.sign-in    6.write    7.read    99.end: ')
        if userInput.isdigit(): menuNum = int(userInput)
    else:
        userInput = input(f'\n[{session.signInedMemberId}] 3.modify    4.delete    5.sign-out    6.write    7.read    99.end: ')
        if userInput.isdigit(): menuNum = int(userInput)

   
   
    if menuNum == config.SIGN_UP:
        print('--- 1.sign-up ---')
        uId = input('Please input new member ID: ')
        uPw = input('Please input new member PW: ')
        uMail = input('Please input new member MAIL: ')
        uPhone = input('Please input new member PHONE: ')

        
        member_db.memberDB[uId] = {
            'uId': uId, 'uPw': uPw, 'uMail': uMail, 'uPhone': uPhone
        }
        
        diary_db.diaryDB[uId] = [] 

        print('New member sign-up success!!')
        if config.DEV_MOD:
            print(f'memberDB: {member_db.memberDB}')
            print(f'diaryDB: {diary_db.diaryDB}')

    
    elif menuNum == config.SIGN_IN:
        print('--- 2.sign-in ---')
        uId = input('Please input member ID: ')
        uPw = input('Please input member PW: ')

        if uId in member_db.memberDB:
            if member_db.memberDB[uId]['uPw'] == uPw:
                print('sign-in success!!')
                session.signInedMemberId = uId 
            else:
                print('sign-in fail!! -- PW error')
        else:
            print('sign-in fail!! -- ID error')

   
    elif menuNum == config.MEMBER_MODIFY:
        print('--- 3.modify ---')
        uPw = input('Please input new member PW: ')
        uMail = input('Please input new member MAIL: ')
        uPhone = input('Please input new member PHONE: ')
        
        currentId = session.signInedMemberId
        memberInfo = member_db.memberDB[currentId]

        memberInfo['uPw'] = uPw
        memberInfo['uMail'] = uMail
        memberInfo['uPhone'] = uPhone

        print(f'>> [{currentId}] info modified!!')

   
    elif menuNum == config.MEMBER_DELETE:
        print('--- 4.delete ---')
        currentId = session.signInedMemberId
        
        
        del member_db.memberDB[currentId]
        
        if currentId in diary_db.diaryDB:
            del diary_db.diaryDB[currentId]

        print('>> Member info & Diary deleted!!')
        session.signInedMemberId = '' 

    
    elif menuNum == config.SIGN_OUT:
        print('--- 5.sign_out ---')
        session.signInedMemberId = ''
        print('Successfully signed out.')

    
    elif menuNum == config.DIARY_WRITE:
        print('--- 6.write ---')
        if session.signInedMemberId == '':
            print('Sorry, Please sign-in first!!')
        else:
            while True:
                diaryTxt = input('10글자 이하의 짧은 일기를 작성하세요 (취소:q): ')
                if diaryTxt.lower() == 'q': break
                
                if len(diaryTxt) > 10:
                    
                    print(f'10글자 초과했어요. (현재 {len(diaryTxt)}자)')
                    continue 
                
               
                diary_db.diaryDB[session.signInedMemberId].append(diaryTxt)
                print('Diary saved successfully!')
                break  

    
    elif menuNum == config.DIARY_READ:
        print('--- 7.read ---')
        if session.signInedMemberId == '':
            print('Sorry, Please sign-in first!!')
        else:
            currentId = session.signInedMemberId
            myDiaries = diary_db.diaryDB.get(currentId, [])

            deepCopyedDiaries = copy.deepcopy (myDiaries)
            deepCopyedDiaries.reverse()
            
            
            for idx, diaryTxt in enumerate(myDiaries):
                    print(f'{idx+1}. {diaryTxt}')
            print('-----------------------------')

    
    elif menuNum == config.SYSTEM_OUT:
        print('99.end - Program terminated.')
        flag = False















































































































