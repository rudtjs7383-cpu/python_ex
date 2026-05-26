# 1.숫자 5개를 리스트에 저장한 뒤 가장 큰 숫자 출력하기
# [3, 7, 1, 9, 5]
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
# number_high = [5,1,7,3]
# number_high.sort()
# print(f'오름차순은 다음과 같습니다.: {number_high}')
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
# for studentace in studentaces:
#   total += studentace
#   average = total /len(studentaces)

# 
# print(f'합계 : {total}')
# print(f'평균 : {average}')
# 

# 7. 리스트에서 가장 작은 숫자 찾기
#  (min() 사용 금지)\
# numbers = [3,7,1,9,5]
# minnum = numbers[0]
# 
# 
# for num in numbers:
#   if num <  minnum:      
#    minnum = num
# 
# 
#   print(f'가장 작은 숫자 : {minnum}')


# 8. 1부터 100까지 숫자 중
# 3의 배수와 5의 배수 출력하기
# for i in range(1,101):
#   if i % 3 == 0:  
    #   print(f'3의 배수 입니다: {i}')
    #   if i % 5 == 0:
        #  print(f'5의 배수 입니다: {i}')
            # 
# 

# 

# 9. 사용자가 입력한 숫자를 리스트에 저장하다가
# 0 입력하면 종료 후 리스트 출력하기
# [입력: 3 ,입력: 7, 입력: 2 ,입력: 0]
# 
# numbers =[]
# 
# while True:
#  userinputdata = int(input('사용자의 숫자를 입력하세요 0을 입력하면 즉시 종료합니다.  :'))
#  if userinputdata == 0:
#    break
# numbers.append(userinputdata)
# print(f'userinputdata:{userinputdata}')
# 

# -PC방 자리 관리 프로그램 

# 너는 PC방 사장이다.
# 손님이 자리에 앉으면 "사용중" 으로 바뀌고, 비어있으면 예약할 수 있다.

# seats = {
    # 1: "빈자리",
    # 2: "사용중",
    # 3: "빈자리",
    # 4: "사용중",
    # 5: "빈자리"
# }
# selectspace = int(input('사용하실 번호를 입력하세요.'))
# if selectspace in seats:
    # if seats[selectspace] == "빈자리":
        # seats[selectspace] = "사용중"  # 상태 업데이트
        # print(f"{selectspace}번 좌석 예약이 완료되었습니다.")
    # else:
        # print(f"죄송합니다. {selectspace}번 좌석은 이미 사용 중입니다.")
# else:
    # print("존재하지 않는 좌석 번호입니다.")

# 프로그램 요구사항
# 1.현재 자리 상태를 전부 출력하기
# print(f'현재 자리의 상태는: {seats}')

# 2. 사용자에게 원하는 자리 번호 입력받기
# 3.예약할 자리 번호 :
# 4.빈자리라면 "예약 완료" 출력 해당 자리 상태를 "사용중" 으로 변경 이미 사용중이라면 이미 사용중인 자리입니다 출력
# 5.예약 후 전체 자리 상태 다시 출력하기.


# - 배달 주문 통계 프로그램 
# 배달 앱에서 하루 주문 데이터를 분석하려고 한다.
# 주어진 주문 목록
order ={
  "치킨" :2,
  "피자" :3,
  "치킨" :4,
  "햄벅": 6,
  "피자" :2,
  "치킨": 1
}
# 프로그램 요구사
from collections import Counter
item = {'치킨': 7,'피자':5,'햄벅':6}
result = Counter(item)
bestseller = max(item, key=item.get)
print(f'가장 많이 주문된 음식은 {bestseller}')
print(f'해당 음식들의 총 주문수는 {result}')
# 1. 각 음식이 몇 번 주문됐는지 딕셔너리에 저장하기
# 2. 가장 많이 주문된 음식 찾기
# 3. 총 주문 개수 출력하기
# 4. 사용자가 음식 이름 입력하면
# 몇 번 주문됐는지 출력하기


# -시험 결과 분석 프로그램 
# 학원에서 시험 결과를 분석하려고 한다.
# 주어진 데이터
scores = {
    "민수": 88,
    # "지훈": 72,
    "수아": 95,
    "유진": 64,
    "서연": 100
}
# 프로그램 요구사항
# 1.전체 학생 점수 출력하기
# 2.평균 점수 계산하기
# 3.최고 점수 학생 찾기
# 4.60점 이상은 합격, 미만은 불합격 출력하기
# 5.90점 이상 학생 수 출력하기
# 6.점수 높은 순으로 학생 출력 도전하기