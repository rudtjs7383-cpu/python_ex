#튜플은 리스트와 같이 데이터를 묶어서 저장하는 컨테이너 자료형입니다
#리스트는 객체(데이터)를 수정할수는 있지만 튜플은 객체(데이터를)수정할수없습니다. 그렇기때문에 변하지않는 데이터를 기입할때엔 튜플을 사용합니다

# fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
# 
# print(f'fruits = {fruits}')
# print(f'fruitstype = {type (fruits)}')

# 튜플 조회

# '''
# 튜플은 아이템의 수정이 불가능하기 때문에 아이템의 삽입 삭제 정렬등의 기능은없고
# 조회하는 기능을 주로 사용합니다.
# 
# '''
# fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
# 
# print(f'{fruits[3]}')
# 
# 
# sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')
# 
# for idx, item in enumerate(sports):
    # if idx % 2 == 1 :
        # print(f'idx : {idx}, item :{item}')
# 


# 특정 아이템의 인덱스 (index)조회
# 튜플 내 특정 아이템의 인덱스를확인할때는, index()함수를 입력합니다.
# fruits = ('사과', '포도', '수박', '참외', '배', '자두', '복숭아', '바나나')
# print(f'idx: {fruits.index('바나나')}')                      #7


#quiz) 아이템 값으로 인덱스 출력하기
#names튜플에서 사용자가 선수이름을 입력하면 이름에 해당하는 인덱스를 출력하는 프로그램만들기
# names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')

# inputData = input(f'선수 이름 입력 : ')
# print(f'이름 : {inputData} 인덱스: {names.index(inputData)}')

#튜플 안의 아이템 유/무 확인하기
#in과 not in 키워드를 사용하면 튜플 안에 특정 아이템의 존재 유/무 를 확인할수있다.

# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# print(f'{'Green' in colors}')
# if 'Green' in colors:
#  print(f'color 에는 Green이 있습니다')
# else:
#  print(f'color에는 Green이 없습니다.')
# 
# 
# 
#  if 'Green' not in colors:
#   print(f'color 에는 Green이 없습니다')
#  else:
#   print(f'color에는 Green이 있습니다.')



#Quiz) 학사 경고 프로그램 만들기
# '''


# scores는 1학기 성적을 튜플로 나타낸 것입니다. F 학점이 있으면 ‘경고’를 출력하는 프로그램을 만들자!
# scores = ('A', 'A+', 'B', 'B-', 'F')
# 
# '''
# scores = ('A', 'A+', 'B', 'B-', 'F')
# if 'F' in  scores:
    # print(f'경고!!!')
# else:
    # print(f'경고 없음!!')
# 
# 
# scores = ('A', 'A+', 'F','B', 'B-', 'F')
# fint = scores.count('F')
# print(f'F학점 개수 : {fint}')



# num1 = [ 1 ,2 , 3]
# num2 = [ 10 , 20 , 30]
# 
# num1.extend(num2)
# print(f'num1: {num1}')
# print(f'num2: {num2}')

# result = num1 + num2
# 
# print(f'값:{result}')





#tuple if~
num1 =  10
num2 = num1

num1 = 100
print(f'num1  : {num1}')
print(f'num2  : {num2}')

# num1 =  [1,2,3]
# num2 =  num1
# print(f'num1 --- : {num1}')
# print(f'num2 --- : {num2}')

num1 =  [1,2,3]
num2 = [0,0,0]
num1[0] = 100
print(f'num1 : {num1}')


for idx , num in enumerate(num1):
    num2[idx] = num
print(f'num1 : {num1}')
print(f'num2 : {num2}')

num1[0] = 100
print(f'num1 : {num1}')
print(f'num2 : {num2}')


print(f'deep copy ---------------------------------------------------------')
#깊은복사 코드 예시

# import copy

# a = [1,2,3,4,5]
# b = copy.deepcopy(a)
# 
# b[0] = 100
# print(f'a : {a}')     #a : [1, 2, 3, 4, 5]
# print(f'b : {b}')     #b : [100, 2, 3, 4, 5]
# 
# 
# a = [1,2,3,4,5]
# b = a.copy()
# 
# b[0] = 100
# print(f'a ------: {a}')     #a : [1, 2, 3, 4, 5]
# print(f'b ------: {b}')     #b : [100, 2, 3, 4, 5]


#슬라이싱
# animals = ('호랑이', '사자', '곰', '여우', '늑대')
# print(f'animals : {animals}')
# 
# print(f'animals : {animals[:3]}')
# print(f'animals : {animals[-1:4]}')
# print(f'animals : {animals[:-2]}')
# print(f'animals : {animals[-1:-2]}')
# print(f'animals : {animals[-3:-1]}')
# 

# 슬라이싱 연습하기
'''
fruits 튜플에서 주어진 요구사항에 맞게 슬라이싱해봅시다.
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
 - 인덱스 2부터 4까지의 아이템을 출력하시오.
 - 인덱스 0부터 3까지의 아이템을 출력하시오.
 - 인덱스 3부터 끝까지의 아이템을 출력하시오.
'''
fruits = ('apple', 'banana', 'plum', 'watermelon', 'peach')
print(f'fruits: {fruits}')

print(f'fruits [2~4]: {fruits[2:5]}') # 인덱스 2~4 까지의 아이템을 출력하세요 fruits [2:5]: ('plum', 'watermelon', 'peach') 
print(f'fruits [0~3]: {fruits[0:4]}') # 인덱스 0~3 까지의 아이템을 출력하세요 fruits [0~3]: ('apple', 'banana', 'plum', 'watermelon')
print(f'fruits [3~끝]: {fruits[3:5]}') # 인덱스 3~끝 까지의 아이템을 출력하세요 fruits [3~4]: ('watermelon', 'peach')


#리스트와 튜플간 변화(형변환,casting)
# '''
# 불가피하게 튜플의 아이템을 수정하려면 리스트로 변환해야 합니다.
# 또한 리스트로 선언된 데이 터를 수정이 안 되게 하려면 튜플로 변환해야 합니다.
# 다음은 데이터 변환을 통해 리스트와 튜플을 변환하고 있습니다.
# '''
# 
# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# 
# orange = 오렌지
# colors = list(colors)
# print(f'color type : {type(colors)}')
# 
# colors[1] = "오렌지"
# print(f'colors : {colors}')
# 
# colors = tuple(colors)
# print(f'colors : {colors}')
# 
# print(f'color type: {type(colors)}')
# 


#quiz)튜플 정렬하기

#colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# 
# colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
# colors =list(colors)
# print(f'변경확인 :{type(colors)}')
# 
# colors.sort()
# print(f'오름차순 확인: {colors}')
# 
# colors = tuple(colors)
# print(f'튜플로 변경 확인: {type(colors)}')
# 
# print(f'오름차순 및 튜플 확인 : {colors}')
# 


colors = ('Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple')
cs = tuple(sorted(colors))
print(f'cs : {cs}')
print(f'cstype :{type(cs)}')
