# 컨테이너 자료형 
# 여러개의 데이터를 묶어서 관리하는 것을 의미한다.
# fruit1 = "사과"
# fruit2 = "포도"
# fruit3 = "복숭아"
# 
# fruits = ["사과","포도","복숭아"] #컨테이너 자료형 : list(리스트)
# print(f'fruits : {fruits}')
# print(f'fruits type : {type (fruits)}')
# 
# 파이썬에서 컨테이너 자료형으로는 리스트(list)튜플(tuple)딕셔너리(dictionary)가 있다.
# 
# 
# 리스트 (list)[] (정의 선언 + 초기화)
# fruits = ["사과","포도","복숭아"]
         #0    # 1     #2
        # ["사과","포도","복숭아"]
# # 인덱스 (index) : 아이템에 부여된 아이템 식별 번호
# 
# 아이템 조회
# 
# fruits[1]
# print(f'fruits[1] : {fruits[1]}')      #포도
# fruits[2]
# print(f'fruits[2] : {fruits[2]}')     #복숭아
# fruits[0]
# print(f'fruits[0] : {fruits[0]}')       #사과
# 
# fruits[3]
# print(f'fruits[3] : {fruits[3]}') #list idex out of range error 발생
# 
# 
# 
# 리스트의 길이 (아이템,개수)
# cmt =  len(fruits)
# print(f'cmt : {cmt}')
# 
# 
# 리스트의 마지막 아이템의 인덱스 값은 리스트의 길이 -1 이다.
# print(f'last data : {fruits , len(fruits)-1}')
# 
# 리스트의 전체 데이터 조회
# 리스트는 반복가능한 객체(데이터)입니다. --> 이터러블한 데이터
# 
# for fruit in fruits:
#   print(f'fruit : {fruits}')
# for idx in enumerate (fruits):
    # print(f'index :{idx} , fruit : {fruit}')
# 

#아이템 삽입
#리스트 마지막에 삽입
# fruit = ['사과','포도','복숭아']
# fruit.append ('수박')
# print(fruit) 
# 특정위치 삽입
# fruit.insert(2,'자두')
# print(fruit)

#리스트 삽입

# list1 = [1,2,3,4]
# list2 = [10,20,30,40,]
# 
# list1.extend(list2)
# print(f'list1 : {list1}')
# print(f'list2 : {list2}')
# 
# list3 = list1 + list2 
# print(f'list3 : {list3}')
# 
# 

#아이템 삭제하기

# sports = ['foootball','baseball','volleyball','basketball']


#마지막 아이템 삭제하기

# sports.pop()
# print(f'sports : {sports}')
# 



#특정위치의 아이템 삭제하기.
# sports.pop(1)
# print(f'sports : {sports}')
# 
# 
#pop()과 비슷하게 사용할 수 있는 키워드 del
# del sports[1]
# print(f'sports : {sports}')
# 
#
#
#pop(),del
#
# nums = [1,2,3,4,5,6]
# deletenum = nums.pop(3)
# print(f'deletenum : {deletenum}')
# 
#특정아이템을 삭제 by 아이템

# languages = ['c/c +','c#','java','python']
# 
# languages.remove('java')
# print(f'languages : {languages}')

# languages = ['c/c +','c#','java','python','java']
# languages.remove('java')
# print(f'languages : {languages}')  #['c/c +','c#','java','python','java'] 에서 중복되는 객체가있을때는 먼저있던 객체가 지워진다.

#quiz)과일 리스트에서 야채를 찾아 삭제하기
'''
다음은 냉장고에 있는 과일을 리스트로 나타낸것입니다.
['사과','망고','당근','수박','포도','참외','토마토']
이 중 과일이 아닌 당근과 토마토를 찾아 삭제하는 프로그램을 만드세요

'''
# fruits = ['사과','망고','당근','수박','포도','참외','토마토']
# print(f'fruits :{fruits}')
# 
# for item in fruits:
    # if item == '당근' or item == '토마토':
    #  fruits.remove(item)
# print(f'fruits : {fruits}')


#quiz) 합격 여부 판정하기
'''
다음은 홍길동 수험생의 2020년 공인중개사 자격증 시험 성적표입니다.
아래 합격 기준에 만족하는지 구하는 프로그램을 만들어봅시다.
- 매 과목 100점을 만점으로 하여, 매 과목 40점 이상
- 전 과목 평균 60점 이상 득점

홍길동 수험생 성적표
부동산 개론: 55점
  민법:     35점
  공법:     40점
  공시법:   70점
  사법:     65점
중개사법:    30점

'''


scores = [55,65,40,70,65,70]

total        = 0
undersubject = 0
averrage     = 0


for score in scores:
     total += score

if score < 40:
    undersubject += 1
print(f'40점 미만 과목 수: {undersubject}')
averrage = total / len (scores)
print(f'평균 :{total / len(scores):.2f}')
# print(f'평균 : {total / 6}')
if undersubject > 0 or averrage < 60:
   print(f'아쉽습니다 다음 기회에...')

else:
   print(f'축! 합격! ')