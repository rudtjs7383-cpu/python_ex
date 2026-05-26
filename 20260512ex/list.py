#container data type (컨테이너 데이터 타입 혹은 컨테이너 자료형)
# 1. list []로 이루어진 자유로운 데이터 타입
# 2. tuple ()로 이루어진 고정된 데이터 타입
# 3. dictionary {}로 이루어진 key와 value로 이루어진 데이터 타입
#

# fruits = ['사과', '수박', '포도', '참외', '배' , '자두 ', '복숭아', '바나나']  #list type
# print (f'fruits : {fruits}')
# print (f'type of fruits: {type(fruits)}')  # list의 첫 번째 요소
# 
# '''
# 리스트에 포함되는 데이터는 어떤 자료형이든 상관없습니다.
# 예를 들어, 리스트 안에 문자열, 숫자, 불리언, 심지어 다른 리스트로 묶일 수도 있습니다.
# '''
# 
# complexlist = [10 , 3.14, 'a' , 'hello']
# 이렇게 하나의 리스트에 다양한 데이터 파일을 넣을 수 있는 프로그램은
# 파이썬과 javascript뿐이다. 일반 java나 c++에서는 불가능하다.

# print (f'complexlist : {complexlist}')
# print (f'type of complexlist: {type(complexlist)}')  # list의 첫 번째 요소
# 
# member = []
# 
# fruits = ['사과', '수박', '포도', '참외', '배' , '자두 ', '복숭아', '바나나']  #list type
# print (f'member : {member}')
# print (f'type of member: {type(member)}')  # list의 첫 번째 요소


# locations  = ("160.1214782", "37.1234567") # tuple type
# print (locations)
# 
# book = {"title": "Graph Theory", "author": "Harry"}
# print (book) 
# 

#ex) 다음 회의 참여자 명단을 리스트로 선언하고 attendees라는 변수에대해 알아보자.
# attendees = ['김철수', '박영희', '이민호', '최지우', '홍길동', '김민우']


# 리스트의 아이템 조회
# 특정 아이템 조회
            # 0     #1      #2     #3     #4     #5      #6        #7
# fruits = ['사과', '수박', '포도', '참외', '배' , '자두 ', '복숭아', '바나나']
# print(f'fruits[3]: {fruits[3]}')
# print(f'fruits[1]: {fruits[1]}')
# print(f'fruits[0]: {fruits[0]}')
# print(f'fruits[8]: {fruits[8]}')    #index error 발생, 리스트의 범위를 벗어남


#리스트 길이 (아이템 개수)조회
'''
리스트 길이란 리스트의 아이템 개수를 뜻하는것으로 len() 함수를 이용하여 구할 수 있습니다.
다음은 len() 함수를 이용하여 리스트의 길이를 구하는 예시입니다.

'''
# numbers = [1, 2, 3, 4, 5]   
# print(f'numbers: {numbers}')
# print(f'len(numbers): {len(numbers)}')
# 
# 
# numbers = [1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 90]  
# 첫번째 데이터 조회
# print(f'첫번째 데이터: {numbers[0]}')
# 마지막 데이터 조회
# print(f'마지막 데이터 : {numbers[len(numbers)-1]}')
# 
# 
# len() 함수는 문자열의 길이를 구하는데에도 사용할수 있다.
# str = "Hellll    llll    lllllllllll llooooo"
# print(len(str))

#quiz) 입력한 글자 수 확인하기

# '''
# 사용자로부터 문자열을 입력받아 입력한 글자 수를 출력하는 프로그램을 작성하세요.
# '''
# 
# user_input = input('메세지를 입력하세요: ')
# user_inputlen = len(user_input)
# print(f'입력 글자 수: {user_inputlen}')
# 
# 
#리스트 전체 데이터 조회
# idx = 0
# 
# balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# for idx , item in enumerate (balls):          #item => '야구공' , item => '축구공' item => '탁구공' item => '골구공' item => '농구공'
  # print(f'item :{item}, index : {idx}')                #0             #1              #2              #3                #4
  # idx += 1
#
# print(f'{balls[0]}')
# print(f'{balls[1]}')
# print(f'{balls[2]}')
# print(f'{balls[3]}')
# print(f'{balls[4]}')

# 
# balls = ['야구공', '축구공', '탁구공', '골프공', '농구공']
# 
# i = 0
# while 1< len(balls):
    # print(f'item : {balls[i]}, idex : {i}')
    # i+= 1


# quiz)다음 리스트에서 마지막 인덱스 값을 출력하는 프로그램을 만드세요
# sports = ['baseball',' basketball' , 'tennis','golf','soccer']
# lenvar = len(sports) -1
# 
# print (sports[lenvar])

#quiz) 다음 리스트에서 python 문자열의 인덱스 값을 출력하는 프로그램을 만들어라.
# launguages = ['c/c+', 'c#','python','java'] 
# for idx , str in enumerate (launguages):
    # if str == 'python':
        # print(f'python idx :{idx}')
# 
# 
# targetidx = launguages.index('python')
# print(f'target idx :{targetidx}')  
# 


#아이템 기존 리스트에 삽입
# 리스트 마지막에 삽입

# sports = ['football','baseketball','vollyball']
# print(f'sports : {sports}') #['football','baseketball','vollyball']
# 
# sports.append ('basketball')
# print(f'sports : {sports}')
# print(f'sports length : {len(sports)}')


#  quiz)취미 추가하기
'''
취미들을 저장할 리스트를 정의하고 사용자가 입력한 취미가 추가되는 프로그램을 만들어보자
그리고 취미의 개수를 출력하자

'''

# hobbies =[]
# 
# while True:
    # 
#  hobby = input('취미 입력:')
#  hobbies.append (hobby)
#  print(f'hobbies: {hobbies}')
#  selectmenunumber = int(input('1.취미 추가'  '2.종료'))
#  if selectmenunumber == 2:
  # print(f'총 갯수 : {len(hobbies)}')
  # break
# 
'''
취미 입력 :  축구
hobbies : ['축구']

'''
#특정 위치에 아이템 삽입
# 리스트의 원하는 위치에 아이템을 삽입할 때는 insert() 함수를 이용합니다.

# countries = ['korea','china','japan']
# countries.insert (1, 'usa')
# print(f'countries : {countries}')

#quiz) 누락된 숫자 추가하기
# numbers = [1,2,3,4,5,7,8,9]
# numbers.insert (5,6)
# print(f'numbers : {numbers}')
# numbers.append(9,10)
# print(f'numbers : {numbers}')
# 
#리스트 연결하기
#리스트와 또 다른 리스트를 연결할때는 extend()함수를 사용합니다.

# list1 =[1,2,3]
# print(f'list1 : {list1}')                                # 1, 2 ,3
# 
# list2 = [10,20,30]
# print(f'list2 : {list2}')                               #10, 20 , 30
# 
# list1.extend(list2)
# print(f'list1 : {list1}')                              # 1,2,3,10,20,30   
# print(f'list2 : {list2}')                              # 10,20,30
# 
# ---------------------------------------------------------------
# 
# print(f'list3 : {list3}') 
# list1 = list1 + list2
# print(f'합계는 : {list1}')

#리스트 아이템 삭제하기
#리스트 마지막 아이템 삭제
 

# sports = ['football','baseball','volleyball','basketball']
# print(f'sports : {sports}')
# sports.pop()
# print(f'sports : {sports}')
# sports.pop(1)
# 
# removeditem = sports.pop()                         
# print(f'removeditem : {removeditem}')


#pop() 대신 del 키워드를 이용해서 아이템을 삭제할수있다.

# sports = ['football','baseball','volleyball','basketball']
# del sports[2]
# print(f'sports : {sports}')



# quiz) sports 리스트에서 'volley ball'을 삭제하는 프로그램을 만들자

# sports = ['football','baseball','volleyball','basketball']
# volleyballidx =  sports.index('volleyball')
# sports.pop (volleyballidx)
# print(f'sports : {sports}')
# numbers = [10, 20 ,30 ,40, 50]
# print(f'numbers : {numbers}')
# 
# fruits = ['사과','바나나','딸기','자몽']
# print(f'fruits[1]: {fruits[1]}')
# 
# animals = ['dog','tiger','lion']
# animals[0] = "cat"
# animals.append('hippo')
# print(f'animals : {animals}')
#  빈 리스트를 만들고 문자열을 추가
# txt = ['python']
# print(f'{txt}')

#다음 리스트의 값을 한줄씩 출력
# num = [1,2,3,4,5]
# for n in num:
#  print (n)

# 다음 리스트에서 짝수만 추출하기
# numbers = [3, 6, 9, 12, 15, 18]
# setnumbers = []
# 
# for n in numbers:
  # if n % 2 == 0:
    # setnumbers.append(n)
  # print(setnumbers)  

# 리스트에 할당된 수에서 홀수를 구하기
# numbers = [1, 8, 12, 15, 18, 23]
# setnumbers = []
# 
# 
# for n in numbers:
  # if n % 2 != 0:
    # setnumbers.append(n)
  # print(setnumbers)  

#그렇다면 모든 할당된 리스트의 숫자에서 홀수와 짝수를 출력한다면?
# numbers = [1,3,4,5,7,9,11,13,14,15,16,20,21,23,25,28]
# evens = []  # 짝수를 담을 바구니
# odds = []  # 홀수를 담을 바구니
# 
# for n in numbers:
    # if n % 2 == 0:
    #  evens.append(n)
# 
# else:
    # odds.append(n)
    # print(odds)
    # print(evens)
# 
# 
# 




















