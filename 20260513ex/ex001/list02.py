# 리스트 정렬
'''
sort() 함수는 리스트의 아이템을 정렬하는데 사용합니다.
reverse 옵션이 False면 오름차순 (ABC), True면 내림차순(DESC)으로 정렬합니다.
'''
numbers =  [5,1,3,4,2,6,]
# print(f'numbers : {numbers}')
# numbers.sort()
# print(f'numbers : {numbers}')

# numbers.sort(reverse=True)
# print(f'numbers : {numbers}')
# 
# 
# korean = ['감','사','합','니','다']
# 
# korean.sort ()
# print(f'korean: {korean}')
# 
# korean.sort(reverse=True)
# print(f'Korean reverse : {korean}')
# 
# scores = [90, 100, 88, 85, 95, 92, 70, 75, 100, 92, 78, 80, 75, 95, 90, 100, 84]
# print(f'scores : {scores}')
# 
# scores.sort()
# print(f'scores : {scores}')
# 
# scores.sort(reverse=True)
# print(f'scores : {scores}')

# quiz) 회의 참석자 정렬하기
# 다음은 회의 참석자 명단입니다. 참석자 명단을 오름차순과 내림차순으로 정렬해봅시다.
# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']

# names = ['홍길동', '김길동', '이길동', '박길동', '정길동']
# names.sort ()
# print(f'names :{names}')
# 
# names.sort(reverse=True)
# print(f'names :{names}')


# 리스트 순서 뒤집기
# reverse() 함수를 이용하면 리스트의 아이템을 역순으로 뒤집을수있다.

# vegetables = ['당근', '오이','양파','감자', '고구마']
# 
# vegetables.reverse()
# print(f'vegetables : {vegetables}')


# 리스트 슬라이싱[slicing](*********************************)
# 슬라이싱 이란 , 리스트에서 필요한 부분의 아이템만 뽑아내는것을 말합니다.
# animals = ['호랑이','사자','곰','여우','늑대']
# print(f'animals : {animals}')
# 
# print(f'animals : {animals[1:4]}')
    #   
# sliceanimals = animals[1:4]
# print(f'animals : {sliceanimals}')
# 
# 

# animals = ['호랑이','사자','곰','여우','늑대']
# print(f'animals : {animals[:3]}')   #슬라이싱에서 시작범위를 생략하면 맨 처음인 0부터 시작한다.
# 
# 
# print(f'animals : {animals[3:]}')  #[시작범위:마지막범위:단계(스텝)]
# 
# print(f'animals : {animals[-1:-2]}') 
# 
# print(f'{animals [::1] }') 
# 

#quiz ) 다음 리스트를 보고 답하세요.
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
#alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 역순으로 출력하세요.
# 
# alphabet.reverse()
# print(f'alphabet : {alphabet}')

#quiz ) 다음 요구사항에 맞게 alphabet 리스트를 슬라이싱하십시오
'''
 - 인덱스 2부터 5까지의 아이템을 출력하시오.
 - 인덱스 0부터 4까지의 아이템을 출력하시오.
 - 인덱스 3부터 7까지의 아이템을 출력하시오.
 - 인덱스 5부터 끝까지의 아이템을 출력하시오.
 - 인덱스 3부터 8까지의 아이템을 출력하시오.
# 
# '''
# 
# print(f'{alphabet[2:6]}') #2부터 5까지의 데이터
# 
# print(f'{alphabet[0:5]}') # 0부터 4까지의 데이터
# 
# print(f'{alphabet[3:8]}') # 3부터 7까지의 데이터
# 
# print(f'{alphabet[5:]}')  # 5부터 끝까지의 데이터
# 
# print(f'{alphabet[3:9]}') # 3부터 8까지의 데이터
# 
# 
# 뒤에서 네개의 아이템을 뽑아서 출력하시오
# print(f'{alphabet[len(alphabet)-4:]}')
# print(f'{alphabet[len(alphabet) -5:]}')

# del alphabet[1:4]
# print(f'del alphabet:{alphabet}')
# 
# 
# animals = ['호랑이','사자','곰','여우','늑대','낙타','판다','도마뱀','토끼']
# 
# print(f'animals : {animals[1:9:2]}')





# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
#  [3, 7, 1, 9, 5]
# num = [3,7,1,9,5]
# 
# maxnum = max(num)
# print(f'가장 큰 숫자는{maxnum}입니다.')
# 


# 2. 사용자에게 숫자 입력받아서
# 1부터 입력한 숫자까지 합계 출력하기 ( 5 )
# userinputnum = int(input(f'숫자를 입력하세요 : '))
# total = 0
# 
# for p in range(1 , userinputnum +1):
#    total += p 
#    print(f'1부터 {userinputnum}까지의 합계는 {total}')
# 

# 3. 리스트에 있는 숫자 중 짝수만 출력하기
#  [1,2,3,4,5,6]
# numlist = [1,2,3,4,5,6]
# for n in numlist:
#    if n % 2 == 0:
    #   print(n) 
    # 
# 

# 4. 리스트 숫자를 오름차순 정렬하기
# [5,1,7,3]
# numberhigh = [5,1,7,3]
# numberhigh.sort()
# print(f'오름차순은 다음과 같습니다.: {numberhigh}')
# 
# 5. 리스트 숫자를 내림차순 정렬하기
#  [5,1,7,3]
# numberlow = [5,1,7,3]
# numberlow.sort(reverse=True)
# print(f'내림차순은 다음과 같습니다.: {numberlow}')
# 
# 6. 리스트 안 숫자의 평균 구하기 [10,20,30]
# studentaces = [10,20,30]
# total = 0
# average = 0
# vars = 0
# for studentace in studentaces:
    # total += studentace
    # average = total /len(studentaces)
# 
# print(f'합계 : {total}')
# print(f'평균 : {average}')
# 


# 7. 리스트에서 가장 작은 숫자 찾기
#  (min() 사용 금지)\
# numbers = [5, 1, 7, 3, 2, 0 ,-1 , - 9]
# minnum = numbers[0]
# 
# for num in numbers:
    # if num <  minnum:      
    #  minnum = num
# 
# print(f'가장 작은 숫자 : {minnum}')
# 

# 8. 1부터 100까지 숫자 중
# 3의 배수와 5의 배수 출력하기

# for i in range(1,101):
    # if i % 3 == 0  or i % 5 == 0 :
        # print(i)
# 
# 
# 9. 사용자가 입력한 숫자를 리스트에 저장하다가
# 0 입력하면 종료 후 리스트 출력하기
# [입력: 3 ,입력: 7, 입력: 2 ,입력: 0
# 
# numbers =[]
# while True:
#   userinputdata = int(input('사용자의 숫자를 입력하세요 0을 입력하면 즉시 종료합니다.  :'))
#   if userinputdata == 0:
    #  break
# numbers.append(userinputdata)
# print(f'userinputdata:{userinputdata}')



#이번에 만들 출석부 관리 시스템은 리스트를 이용해서 학급의 학생 명단을 관리하는 프로그램으로, 시나리오에 따라 
#프로그래밍을 전개합니다. 예제가 쉬운 만큼 시나리오만 보고 직접 코딩해 보는 것을 추천합니다



# [[ 시나리오 ]]
 #1 :  학급 학생수가 10명(정우람, 박으뜸, 배힘찬, 천영웅, 신석기, 배민규, 전민수,
 #  박건우, 박찬호, 이승엽)인 리스트를 만든다.
 #2 :  ‘가나다’ 순으로 정렬한다.
 #3 :  ‘박찬호’ 학생이 전학을 가게 되었다. 출석부에서 삭제한 후 전체 학생과 학생 수를 
#  출력한다.
 #4 :  선생님을 돕기 위한 학생으로 앞에서 3명을 뽑는다.
 #5 :  새로운 친구가 전학 왔다. 이름은 ‘이병규’이다.
 #6 :  자리를 바꾸기 위해서 학생 순서를 역순으로 뒤집는다.
 #7 :  ‘정우람’ 학생이 이름을 ‘정잘남’으로 개명했다.


              #0        #1      #2       #3       #4      #5       #6      #7       #8
# students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수','박건우', '박찬호', '이승엽']
# 
# students.sort()
# print(f'학생의 가나다 정렬은 다음과 같다. : {students}')
# 
# 
# students.remove('박찬호')
# print(f'박찬호학생은 전학을갔다, 총 학생수는 :{len(students)}')
# 
# print(f'빠진 출석명단은? : {students}')
# 
# 
# students[0:3]
# print(f'선생님을 도와줄 학생은: {students[0:3]}')
# 
# 
# students.append("이병규")
# students.sort()
# print(f'전학생이추가되었다  {students}')
# print(f'이병규 학생이 추가되었다 총 학생수는 :{len(students)}')
# 
# students.reverse()
# print(f'자리를 바꾸기 위하여 역순 {students}')
# 
# students[1] = "정잘남"
# 
# print(f'정우람 학생이 정잘남이라는 이름으로 개명했다. {students}')
# 




# import random
# random.shuffle(students)
# print(f'students : {students}')




#혈액보관시스템)
# # 혈액 보관 시스템
# '''
# 헌혈 프로그램을 통해서 10명의 기부자에게 혈액을 받아 리스트에 보관하고,
# 보관하고 있는 혈액형을 종류별로 몇 팩씩 보유하고 있는지 한눈에 보여주는 프로그램을 만들어봅시다.
# '''
# 
# LOOP_COUNT = 3
# 
# bloods = []
# 
# for i in range(LOOP_COUNT):
    # print('헌혈해 주셔서 감사합니다. 혈액형을 선택하세요.(A, B, AB, O)')
    # bloods.append(input())
# 
# print(f'bloods: {bloods}')
# 
# print('-' * 30)
# print(f'혈액형\t| 개수')
# print('-' * 30)
# print(f'A형\t: {bloods.count('A')}')
# print(f'B형\t: {bloods.count('B')}')
# print(f'AB형\t: {bloods.count('AB')}')
# print(f'O형\t: {bloods.count('O')}')
# print('-' * 30)