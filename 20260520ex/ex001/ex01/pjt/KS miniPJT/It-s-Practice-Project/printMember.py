# '0.'   메뉴창을 하단과 같이 생성한다.
#  메뉴: 1.회원가입  2.로그인  3.특정 회원 정보 출력  4.모든 회원 정보 출력  5.Id 찾기   6.Pw 찾기  0. 종료

# '1.'   회원가입'을 선택하면 회원 ID, PW ,Email, Phone 정보를 입력받아 가입을 진행함.
# '1-1'  Id, Email, Phone 정보가 중복되는 경우 다음으로 넘어가지 않고 해당 항목을 다시 입력하도록 함
#        ex) 이메일 입력하였는데 이메일이 중복될시 이메일을 다시입력하도록함

# '2.'  '로그인'을 선택하면 ID, PW 를 입력바아 로그인 성공, 실패를 출력함 3회 실패시 프로그램 종료
# '2-1'  로그인 pw 틀릴시 메인으로 돌아오는것이 아닌 id, pw 를 다시입력할수있도록한다.

# '3.'   특정 회원 정보 출력'을 선택하면 회원 ID,PW 를 입력받아 일치하는 회원 정보를 모두 출력

# '4.'   모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.

# '5.'   Id 찾기를 누를시 등록된 이메일로 메일이 발송되었습니다.
#       ex) 'abcd1234@gmail.com'로 메일이 발송되었습니다.

# '6.'   Pw 찾기를 누를시 사용하던 Id를 입력 하고 등록된 이메일을 입력하면 메일로 임시 Pw 발급
#       ex) Pw를 찾을 Id를 입력하세요.
#           등록된 Email을 입력하세요.
#           'abcd1234@gmail.com'로 임시Pw가 발송되었습니다.(텍스트만 발송)

# '0.' '종료'를 선택하면 프로그램을 종료시킨다.

SIGN_UP = 1 
SIGN_IN = 2
PRINT_MY_INFO = 3
PRINT_ALL_MEMBER_INFO = 4
SIGN_IN_ID = 5
SIGN_IN_PW = 6
SYSTEM_SHUTDOWM = 0

DEV_MOD = True
members = {}

if DEV_MOD:
    uIds = ['gildong', 'chanho', 'saeri']
    uPws = ['1234', '5678', '9012']
    uMails = ['gildong@gmail.com', 'chanho@naver.com', 'saeri@daum.com']
    uphones = ['010-1234-5678', '010-9999-8888', '010-7777-6666']
    for n in range(len(uIds)):
        members[uIds[n]] = {
            'uId': uIds[n],
            'uPw': uPws[n],
            'uMail': uMails[n],
            'uPhone': uphones[n]
        }

def getSelectedMenuNum():
    selectedMenuNum = int(input('1.회원가입  2.로그인  3.특정 회원 정보 출력  4.모든 회원 정보 출력  5.Id 찾기   6.Pw 찾기  0. 종료'))
    return selectedMenuNum

def printAllMemberInfo(value):
    for key1, value1 in value.items():
                print(f'{key1}: {value1}')

flag = True
while flag:    
    userSelectedMenuNum = getSelectedMenuNum()
    
    if userSelectedMenuNum == PRINT_MY_INFO:
         uId = input('Input member ID: ')
         uPw = input('Input member PW: ') 
         if uId in members:
             uInfo = members[uId]
             if uInfo['uPw'] == uPw:
                 print('SIGN_IN SUCCESS!')
                 print('-' * 30)            
                 for key, value in uInfo.items():
                     print(f'{key}: {value}')
                 print('-' * 30)
                 updateInfo = int(input('1.아이디 변경  2.비밀번호 변경  3.이메일 변경  4.번호 변경  0.종료'))
                 if updateInfo == 1:
                    updateId =  input('변경할 아이디 입력: ')
                    members[uId]['uId'] = updateId
                    print('아이디가 변경되었습니다.')
                 elif updateInfo == 2:
                     updatePw =  input('변경할 비밀번호 입력: ')
                     members[uId]['uPw'] = updatePw
                     print('비밀번호가 변경되었습니다.')
                     
                 elif updateInfo == 3:
                     updateMail =  input('변경할 이메일 입력: ')
                     members[uId]['uMail'] = updateMail
                     print('이메일이 변경되었습니다.')

                    
                 elif updateInfo == 4:
                     updatePhone =  input('변경할 번호 입력: ')
                     members[uId]['uphone'] = updatePhone
                     print('번호가 변경되었습니다.')
                   
                 elif updateInfo == 0:
                     break
             else:
                 print('SIGN_IN FAIL!') 
         else:
             print('존재 하지 않은 ID입니다. 다시 확인하세요')
    
    elif userSelectedMenuNum == PRINT_ALL_MEMBER_INFO:
        #  로그인 후 정보 확인 할 수 있도록 변경하기
         signInCount = 1 
         while True:
            uId = input('Input member ID: ')
            uPw = input('Input member PW: ')
            if uId in members:
                uInfo = members[uId]
                if uInfo['uPw'] == uPw:
                    print('SIGN_IN SUCCESS!')
                    break
                else:
                    print('SIGN_IN FAIL!') 
                    signInCount += 1
                    if signInCount > 3:
                        print('3회 이상 틀렸어요!')
                        break    
            else:
                print('존재 하지 않은 ID입니다. 다시 확인하세요')
         for key, value in members.items():
             print(f'------{key}님의 정보----------')
             printAllMemberInfo(value)         
             print('-' * 30)