# '''
# C: Create   생성, 추가
# R: Read     조회
# U: Update   수정
# D: Date     삭제
# '''
# 
# '''
# 딕셔너리(Dictionary): {key: value}
# '''
# 
# C: Create
# 
student = {
    '학번': 123456789,
    '이름': '홍길동',
    '나이': 20,
    '성별': 'M',
    '연락처': '010-1234-5678'
}
# 
# print(f'student: {student}')
# print(f'student type: {type(student)}')
# 
# R: Read
# sNo = student['학번']
# print(f'sNo: {sNo}')

# 
# U: Update
# sName = student['이름']
# print(f'sName: {sName}')        # 홍길동 > 홍길자
# 
# student['이름'] = '홍길자'
# sName = student['이름']
# print(f'sName: {sName}')        # 홍길자
# 
# 
# D: Delete
# del student['연락처']
# print(f'student: {student}')
# 
# keys(), values(), items()
# keys(): 딕셔너리 자료형에서 키값들만 몽땅 뽑는다. 
# 뽑은 키들은 리스트와 비슷한 데이터 타입이다.
# 
# keys = student.keys()
# print(f'keys: {keys}')
# print(f'keys type: {type(keys)}')
# 
# for key in keys:
    # print(f'key: value = {key}: {student[key]}')
# 
# values(): 딕셔너리에서 벨류값들만 몽땅 뽑는다. 
# 뽑은 벨류들은 리스트와 비슷한 데이터 타입이다.
# 
# values = student.values()
# print(f'values: {values}')
# print(f'values type: {type(values)}')
# 
# for value in values:
    # print(f'value: {value}')
# 
# items = student.items()         # key & value
# print(f'items: {items}')        # dict_items([('학번', 123456789), ('이름', '홍길자'), ('나이', 20), ('성별', 'M')])
# for item in items:
    # print(f'item: {items}')
    # print(f'item[0], item[1]: {item[0]}, {item[1]}')
# 
# for key, value in items:
    # print(f'key: value = {key}: {value}')
# 
# '''
# key, value = ('학번', 123456789)
# '''
# 
# 구조분해할당
# a, b = (10, 20)
# print(f'a: {a}, b: {b}')
# 
# c = (10, 20)
# a = c[0]
# b = c[1]
# print(f'a: {a}, b: {b}')
# 
# 
# swapping ==> a: 20, b: 10
# temp = a
# a = b       # a: 20
# b = temp    # b: 10
# 
# a, b = b, a
# 
# scores = [10, 20, 30, 40, 50, 60]
# '''
# a = 10
# b = 20
# c = [30, 40, 50, 60]
# '''
# 
# a, b, *c = scores
# 
# print(f'a: {a}')    # a = 10
# print(f'b: {b}')    # b = 20
# print(f'c: {c}')    # c = [30, 40, 50, 60]
# 
# quiz) 다음은 스포츠 센터 회원 정보를 나타낸 표이다.
# 표를 보고 

# 리스트로 형식으로 짜게 되면? 

# members = {
    # '2019-052001': ['박찬호', '25', 'M', '010-1234-5678', '헬스,수영', '0']
# }
# 
# info = members['2019-052001']
# print(f'info: {info}')              # 박찬호+25+M+010-1234-5678+헬스,수영+0
# infos = info.split('+')
# print(f'infos: {infos}')            # ['박찬호', '25', 'M', '010-1234-5678', '헬스,수영', '0']
# 
# print(members['2019-052001'])
# 
# 보기 복잡하니까 딕셔너리로 짜보자 
# 
# members = {
    # '2019-052001': {
        # '이름': '박찬호', 
        # '나이': '25', 
        # '성별': 'M', 
        # '연락처': '010-1234-5678', 
        # '이용서비스': ['헬스, 수영'], 
        # '할인율': '0'}
# }
# 
# print(members['2019-052001'])
# print(members['2019-052001']['이름'])
# print(members['2019-052001']['나이'])
# print(members['2019-052001']['성별'])
# print(members['2019-052001']['연락처'])
# print(members['2019-052001']['이용서비스'])
# 
# 
# '''
# 데이터란?
# 변수
# 연산자
# 제어문(조건문, 반복문)
# 컨테이너형 자료 구조(list, tuple, dictionary)
# '''
# 함수(function)
# python 에서는 함수가 꽃!
# java에서는 클래스가 꽃!
# y = 3x + 5
# x:1 => y:8
# x:2 => y:11
# x:3 => y:14
# 프로그래밍의 함수 또한 수학의 함수와 동일하게 값을 넣어주면 특정 기능을 수행한 연산 결과를 출력합니다, 여기서 특정 기능이란 덧셈 같은 
# 비교적 간단한 연산부터 네트워크 연결, 회원 인증, 메일 발송과 같이 복잡하고 어려운 작업까지 모두 포함합니다.
# 즉 함수란 특정 기능을 하는 코드를 묶어 놓은 것이고 사용저눈 함수에 값을 넣어 결과를 얻습니다.
# 믹서기에 사과를 넣으면 사과 주스가 되고, 오렌지를 넣으면 오렌지 주스가 되듯이 사용자는 함수에 값만 집어넣으면 원하는 결과를 얻을 수 있습니다.
# 코드 재사용 > 함수
# 데이터 재사용 > 변수
# 함수 정의하기
'''
사용자 함수를 만든다는 것을 '함수를 정의한다.' 라고 합니다.
함수를 정의할 때 def 키워드를 사용합니다. 그리고 함수명은 클론(:), 실행부를 이용합니다.
'''
'''
def 함수명():
    실행부(함수 기능)
'''
# def greet():
#     print('안녕하세요.')
#     print('반갑습니다.')
#     print('저는 홍길동입니다.')
'''
함수명 규칙
1. 내장 함수명과 동일하면 안된다.
2. 첫 글자는 주로 소문자로 시작한다.
3. 첫 글자를 숫자로 사용할 수 없다.     1great(): X / g1reat(): O / greet1(): O
4. 특수문자는 사용할 수 없지만 언더바(_)는 사용 가능하다.
5. 두개 이상의 단어가 조합되는 경우 스네이크 또는 카멜표기법을 사용한다.
    sendMessage(): calculateDistance(): 
'''
# quiz) 온도 센서 작동 시스템 만들기
# 온도 센서 작동을 시작하고 멈추는 함수를 정의해봅시다.
# 함수명은 함수의 기능을 이해하기 좋도록 짓습니다.
# def startTemperatureSensor():
#     print('온도센서 작동을 시작합니다.')
# def stopTemperatureSensor():
#     print('온도센서 작동을 정지합니다.')
# # 함수 호출
# startTemperatureSensor()
# stopTemperatureSensor()
# # print(stopTemperatureSensor)        # <function stopTemperatureSensor at 0x0000028914AE3A00>
# # print(startTemperatureSensor)       # <function startTemperatureSensor at 0x0000028914AE3950>
# # quiz) 내 노트북은 몇 인치일까?
# '''
# 고등학교 졸업 기념으로 노트북을 하나 장만했습니다.
# 노트북 사이즈에 꼭 맞는 파우치를 하나 구매하려고 하는데 사이즈 표에 인치로만 표시되어있습니다.
# CM를 인치로 바꿔주는 함수를 만들어봅시다.
# (linch = 0.393701cm)
# '''
# def convertUnit():
#     lengthCM = float(input('길이(cm) 입력: '))
#     print(f'인치: {lengthCM * 0.393701}inch')
# convertUnit()
# convertUnit()
# convertUnit()
# quiz) 이동 거리를 계산하는 함수
'''
길동이는 5시간 동안 3km의 속도로 등산을 했습니다.
길동이가 등산한 시간과 속도를 입력하면 이동한 거리를 계산해주는 프로그램을
함수로 이용하여 만들어봅시다
'''
# def calculateDistance():
#     print(f'이동거리: {hourData * speedData}km')
# hourData = float(input('이동 시간: '))
# speedData = float(input('이동 속도: '))
# calculateDistance()
# # pass 키워드
# def calculateNumber():
#     pass
# 함수 내에서 또 다른 함수 호출
# def fun1():
#     print('fun1() CALLED!!')
# def fun2():
#     print('fun2() CALLED!!')
    
# def fun3():
#     fun1()
#     fun2()
#     print('fun3() CALLED!!')
# fun3()
# '''
# print('fun3() CALLED!!')
# print('fun2() CALLED!!')
# print('fun3() CALLED!!')
# '''
# def fun4():
#     print('fun4() CALLED!!')
#     fun4()
# fun4()      
# def factorial(n):
#     if n == 1:
#         return 1
    
#     return n * factorial(n - 1)
# print(factorial(5))
# quiz) 다국어 인사말 프로그램 by 함수
'''
출신 국가를 선택하면 해당하는 국가의 인사말이 출력되는 프로그램을 함수를 이용해서 만들어봅시다.
1. 한국     2. USA      3. Japan
'''
# def introKor():
#     print('안녕하세요')
# def introEng():
#     print('Hello')
# def introJap():
#     print('こんにちは')
# selectedMenuNum = int(input('where are you from? 1. 한국     2. USA      3. Japan '))
# if selectedMenuNum == 1:
#     introKor()
# elif selectedMenuNum == 2:
#     introEng()
# elif selectedMenuNum == 3:
#     introJap()
# 계산기 프로그램 by 함수
'''
사용자가 숫자 2개를 입력하고 연산자를 선택하면 연산결과가 출력되는 프로그램을 함수로 이용해서 만들어봅시다.
'''
# def add():
    # print(f'덧셈 결과: {inputNumber1 + inputNumber2}')
# def sub():
    # print(f'뺄셈 결과: {inputNumber1 - inputNumber2}')
# def mul():
    # print(f'곱셈 결과: {inputNumber1 * inputNumber2}')
# def div():
    # print(f'나눗셈 결과: {inputNumber1 / inputNumber2}')
# def calculator():
    # if selectedOperator == 1:       # 덧셈
        # add()
    # elif selectedOperator == 2:     # 뺄셈
        # sub()
    # elif selectedOperator == 3:     # 곱셈
        # mul()
    # elif selectedOperator == 4:     # 나눗셈
        # div()
# inputNumber1 = float(input('숫자를 입력하세요: '))
# selectedOperator = int(input('연산자를 선택하세요. 1. 덧셈     2. 뺄셈      3. 곱셈    4. 나눗셈'))
# inputNumber2 = float(input('숫자를 입력하세요: '))
# calculator()