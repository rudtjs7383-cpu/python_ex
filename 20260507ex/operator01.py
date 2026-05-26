# 나눗셈 연산자
# print(10/ 2)                 #5.0  
# print(3.14/ .5)             #6.28 0.5에서 0을 생략할수도있다

# num1 = 100
# num2 = 10
# print(f'num1/num2 = {num1/num2}')


# weight = int(input('몸무게(kg) : '))
# height = int(input('신장(m) : '))
# bmi = weight/(height_m ** 2 )
# print(f'bmi :{bmi}')
# print(f"bmi : {bmi:.2f}")
# 숫자 0을 어떤 수로 나누어도 결과는 항상 0이다.
# print(0 / 123)
# # 어떤 숫자를 0으로 나눌 수 없다. 에러
# print(10 / 0)

# #나머지만  몫 거듭제곱
# print (10 % 2)
# print (10 % 1)


#홀짝게임하기
# 주먹 쥔 손을 상대방에게 내밀며 손 안에 동전개수가 홀수인지 짝수인지 맞춰보자
# 손 안에 동전 개수를 입력하면 짝수는 0, 홀수는 1을 출력하는 프로그램

# inputdata = int(input('손 안에 동전 수를 입력하세요'))
# result = inputdata % 2
# print(result)

# # 몫 //
# print(10 // 3)                          #3
# print(6 // 2)                           #3
# #quiz) 빵을 나누어 줄수 있는 학생 수를 구하자
# #길동이는 97개의 빵을 한사람당 3개씩 나누어준다고 했을때 최대 몇명에게 나누어줄수있는지와 몇개가 남는지 구해보자
# bread = 97
# breadcnt = 3
# maxfriendcnt = bread // breadcnt
# print(f"빵을 나누어 줄 수 있는 학생의 수: {maxfriendcnt}")

# restbreadcnt = bread % breadcnt
# print(f"남은 빵의 갯수: {restbreadcnt}")

# # 거듭제곱 **
# print(2 ** 2)                        #4
# print(2 ** 3)                        #8
# print(2 ** 10)                       #1024

#quiz) 전염병 예상 감염자 수 구하기
# 보건 당국은 전염병의 감염 확산 추세를 파악한 결과,
# 하루에 한 사람이 한 명씩 감염시키는 것으로 나타났습니다.
# 확진자 한 사람이 나올경우 30일 이후에 몇 명의 감염자가 나오는지 계산해봅시다.

# man = 2
# date = 30
# total = man ** date 
# print(f'{date}일 이후 예상 감염자수: {total}명입니다.')

