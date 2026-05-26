# 컨테이너 자료형 (list,tuple,dictionary)에서 dictionary를배워보자.
# 딕셔너리란? 단어적 의미 그대로 사전과 같은 구조를 가지고있다.
#사전에서 단어를찾으면(key), 그 값 혹은 의미(value)를 찾듯 key와 value는 같이 붙어다닌다
# 중괄호{}를 사용하여 선언하고, 딕셔너리(dictionary)는 리스트와 함께 파이썬 프로그램에서
#  많이 사용하는 컨테이너 자료형입니다. 
# 리스트가 인덱스를 이용하여 아이템을 참조한다면, 
# 딕셔너리는 인덱스 대신 키(key)를 이용하여 아이템을 참조합니다.
# 
# 
#{'박찬호','박세리','박지성','이승엽'} = key
#{'48','50','40','43'} = value

# ages = {'박찬호': 48,'박지성':40 ,'박세리': 50 ,'이승엽' : 43}
# key 값 먼저 입력, value값은 무조건 나중
# : (콜론)으로 key : value 구분짓고 ,(콤마)로 이전데이터와 구분하기
# key값은 중복될수없다 하지만 value값은 무한대로 중복이 가능하다.
# if) 나의 가방과 친구가방이 있지만 책의 무게는 40으로 같다 그렇다면 출력이 가능한가?
# 정답은 그렇다, 출력이 가능하다 key의 값이 중복되지 않기 때문이다
# print(f'ages : {ages}')
# print(f'ages type: {type(ages)}')
# scores = {
# 'c/c++'  :  'A', 
# 'java '  :  'B+',
# '네트워킹' : 'C',
# '보안'    : 'A' ,
# '해킹'    : 'F',
# '시스템'  : 'C+'
# }
# 
# print(f'scores : {scores}')

#마지막 내용: (********************************************)
#리스트 튜플 딕셔너리

# listvar = [3, 3.14 , 'hello']
# print(f'listvar : {listvar}')
# 
# tuplevar = ('python',124.123456)
# print(f'tuplevar : {tuplevar}')
# 
# dictvar = {
    # '홍길동' :10,
    # '박찬호' : '열살',
    # '박세리' : 3.14
    # 
    
# }
# print(f'dictvar : {dictvar}')
# 
# listvar1 = [1,2,3]
# listvar2 = [1,2,3, listvar1]
# print(f'listvar1 : {listvar1}')
# print(f'listvar2 : {listvar2}')
# print(listvar2[3][1])           #2차원 배열(2차원 리스트)
# 

# print(type(listvar2[3]))             #list
# print(type(listvar2[3][1]))          #int
# print(type(listvar2[2]))             #int

dicts = {
    'name' : '박찬호',
    'age'  : 20,
    'addr' : '대전중구',
    'hobby': ['축구','농구','배구']
}

print(dicts['name'][:3])


print(dicts['age'])

print(dicts['addr'][:4])

print(dicts)

# '''
# num[][]           #2차원 배열, 3차원까지는 가능하나, 가급적 지양
# '''

