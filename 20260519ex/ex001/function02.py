#지역변수 vs 전역변수
#지역 변수는 함수 내부에서 선언된 변수로 함수내부에서만 사용가능 합니다.
#전역변수는 함수 외부에서 선언된 변수로 함수 내/외부에서 사용 가능합니다.

# num = 10
# 
# def fun():
    # num = 20                         #    지역변수
    # global num   
    # num = num + 1               # 데이터 수정 num(전역변수) = 10 + 1
    # print(f'num :{num}')      #10, 전역변수 num > 20, 지역변수 num 
    # 
# print(f'num: {num}')          #10,전역변수 num
# 
# fun()
# 
'''
global 키워드는 함수 내에서 전역변수의 값을 '수정'하고자 할때 반드시 명시하자!

'''


#quiz) 웹사이트의 누적방문 횟수 프로그램
#웹사이트 방문 여부를 입력받아 웹사이트의 누적 방문 횟수를 출력해봅시다.


# flag = True
# totalvisitor = 0
# 
# 
# def countvisitor():
    # global totalvisitor
    # totalvisitor += 1
# 
# 
# while flag:
#    selectedMenu_num  = int(input('1. 웹사이트 방문        2. 종료'))
#    if selectedMenu_num == 1:
    #    countvisitor()
    #    print(f'누적 방문 횟수: {totalvisitor}')
# 
# 
#    else:
    #    flag = False
    #    print(f'Good bye ! ! ! !')
   


#매개 변수(*********************************************************************)
#매개 : 둘 사이에서 양편의 '관계를 맺어'줌
# 함수를 사용하기 위해 먼저 함수를 정의하고 필요할 때 호출하죠.
# 이 때 함수를 정의하는 쪽을 함수 정의부 (선언부), 함수를 호출하는 쪽을 호출부라고 합니다.

#함수를 호출할 때 데이터를 넘겨줄 수 있는데, 이 데이터를 '인수' 라고합니다.
# 함수 정의 부는 인수를 받으면 '매개변수' 라는 변수에 저장합니다. 그리고 매개변수는 지역 변수의 일종입니다.

# def greet(name,age,address):
    #name = '홍길동' or '박찬호' or '박세리' 
    #age = '25','20','30'  <<이때 사용되는 name, age 는 매개입니다.
    # print(f'{name}님 안녕하세요. 나이는 {age}입니다,주소는{address}')

 
# greet('홍길동',25,'대전시')                  #< 괄호에 들어가는 숫자 혹은 글자가 인수입니다
# greet('박찬호',20,'서울시')
# greet('박세리',30,'공주시')

# def forcastweather(temp,humi,rain):
    # print(f'날씨 예보입니다.')
    # print(f'최고온도는 : {temp}도입니다.')
    # print(f'평균습도는 : {humi}%입니다.')
    # print(f'비올 확률은: {rain}%입니다.')
# 
# 
# forcastweather(35,70,80)
# 
# 인수의 개수를 모르는 경우
# 우리 학급 학생들의 시험점수 총합과 평균을 구하는 함수를 만들자
# 우리 학급 학생수는 총 3명이다.


# 3명 -> 4명
# def printscoresforstudent(score1,score2,score3,):
# totalscore = score1 + score2 + score3  
# averagescore = totalscore / 3

    # print(f'총합 : {totalscore}')
    # print(f'평균 : {averagescore}')

# def printscoresforstudent(subject,*score):                   #리스트(list) > 튜플(tuple)
    # print(f'score type : {type[score]}')
    # print(f'score length :{len[score]}')
    # totalscore = 0
    # for score in score:
        # totalscore += score
#  
# print(f'총합: {totalscore}')
# averagescore = totalscore / len(score)
# print(f'평균 : {averagescore}')
# 
#  


#  
#  

# 
# printscoresforstudent(90,80,100,90)
# 
# 
# quiz) SMS와 MMS 구별하기
'''
문자를 보낼 때 100자 이하인 경우에는 단문 메시지(SMS)로 50원을 부과합니다. 그런데 100자를 
넘어가면 장문 메시지(MMS)로 변경되면서 100원이 부과됩니다. 단문과 장문을 구별해서 돈을 부
과하는 프로그램을 만들어봅시다. 
'''

# def sendusermessage(str):
    # strlength = len(str)
    # print(f'사용자가 입력한 문자길이 : {strlength}')
    # if strlength <= 100:
    #  print(f'SMS 발송완료 !')
    #  print(f'50원 부과!')
    # else:
    #    print(f'MMS 발송 완료!')
    #    print(f'100원 부과 !')
# 
# inputdata = input('문자 입력:')
# sendusermessage(inputdata)    
 
    
    
    

    

# 
    
    
# 선생님이 몇명일지 모르는 학생의 점수를 입력한다.
# 이때 학생점수의 총합과 평균을 구하는 함수를 만들고 이를 이용하는 프로그램을 만들어보자
# flag = True
# studentscores = []
# 
# def printscoreforstudent(scores):        #scores = [,,,,,,,,,,,]
    # if len(scores) == 0:
        # print('학생수가 0명이라 총점과 평균을 구할수없습니다.')
    # else:
        # totalscore = 0
    # for score in scores:
    #  totalscore += score
    #  average = totalscore /len(scores)
    #  print(f'총점 : {totalscore}')
    #  print(f'평균 : {average}')
# 
# while flag:
    # selectedmenunum = int(input('1.학생점수 입력       2.종료  '))
    # if selectedmenunum == 1:
        # score = int(input('학생의 점수 입력:'))
        # studentscores.append(score)
    # else:
        # flag = False
# printscoreforstudent(studentscores)


#인수와 매개변수의 순서가 일치하지 않을 경우

# def printmemberinfo(name,email,major,grade):
    # print(f'name\t: {name}')
    # print(f'email\t: {email}')
    # print(f'major\t: {major}')
    # print(f'grade\t: {grade}')
    # print('------------------------------------------------------')
# 
# printmemberinfo('Hong Gildong','gildong@gmail.com','art',1)    
# printmemberinfo(email='gildong@gmail.com',
                # name='Hong Gildong',
                # major='art',
                # grade=1)    


# def printmemberinfo (info):
#    print(f'name\t: {info['name']}')
#    print(f'email\t: {info['email']}')
#    print(f'major\t: {info['major']}')
#    print(f'grade\t: {info['grade']}
    # memberinfo = ({
    #  'name' : 'hong gil dong',
    #  'email': 'gildong123@gmail.com',
    #  'major' : 'art',
    #   'grade' : 1 ,
    #  }) 
#   
#   
#   
#   printmemberinfo(memberinfo)
#   

#매개 변수의 기본값 설정
# 직원 급여 지급 프로그램을 만들어보자!

# def setSalary(name,pay = 200):
    # print(f'{name}의 급여는 {pay}원 지급 !')
# 
# 
# setSalary('박찬호', 400)
# setSalary('박세리', 600)
# setSalary('박용택', )
# 
# 데이터 반환(Return)
# 데이터 반환이란, 함수는 실행이 끝난 후에 결과물(값)을 호출부로 반환할 수 있습니다.
# 이때 사용하는 키워드가 return입니다.
# 덧셈 연산 함수를 만들어 결과를 출력하는 프로그램을 만들어보자

# def printresult(value):
    # print(f'result : {value}')
# 
# 
# 
# def addFunction(n1,n2):
    # sum = n1+n2
    # print(f'결과 값 : {sum}')
    # printresult(sum)
# 
    # return sum
# 
# 
# addFunction(10,20)
# print(f'result : {result}')
# DEV_MOD = True
# 
# 
# 
# def fun1():
    #  print('1111111111')                #개발 단계에서 디버깅 용도로만 사용한다.
    #  if DEV_MOD == True:
    #   print('2222222222')
    #  print('3333333333')
    #  return
# 
# fun1()    



#별탑 만들기

# def increaseStart(limitStarcount):
    # print('*')
    # print('**')
    # print('***')
    # print('****')
    # print('*****')
    # print('******')
    # return
    # print('*******')
    # print('********')
    # for n in range(1,8):
        # print('*' * n)
        # if n == limitStarcount:
            # break

# # increaseStart(7)

# 7~8교시
# Toy 프로젝트 진행
'''
처음 프로그램이 실행되면 다음과 같은 메뉴를 출력한다.
메뉴 : 1. 회원가입  2.로그인    3. 특정 회원 정보 출력    4.모든 회원 정보 출력    99.종료
사용자가 '1번 회원가입'을 선택하면 회원 ID, 회원PW , 회원 Email, 회원Phone 정보를 입력받아 회원가입 진행한다.
사용자가 '2번 로그인'을 선택하면 회원 ID, PW 를 입력받아 '로그인 성공'혹은 '실패'를 출력한다
사용자가 '3번 특정 회원정보출력'을 선택하면 회원ID와 회원PW를 입력받아 일치하는 회원 정보를 모두 출력한다.
사용자가 '4번 모든 회원 정보 출력'을 선택하면 가입되어 있는 모든 회원 정보를 출력한다.
사용자가 '99번 종료'를 선택하면 프로그램을 종료 시킨다.

심심하면>> 특정회원의 회원ID와 회원 PW를 입력받아 인증되면 회원 정보를 수정하는 기능을 구현해보자!
'''


































































































    



    
    

    
    

    
    
    
    
    
    
   
    
    






























