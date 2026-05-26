# 반복문 (for문),(while문)

# for 문 = ~~을 하는동안
# '''
# for문은 지정된 입력횟수에 따라 결과값을 출력하고, 횟수에 의한 반복에만 쓰임
# while문은 결과값이 참일때만 출력됨, 어떠한 특정 조건에 의한 반복에만 쓰임
# for 문은 for~ in 키워드 범위를뜻하는 range (iterable)반복 가능한 객체를 입력하고, : 클론으로 마무리한다
# 들여쓰기 네칸 후 실행구문을 입력한다. ~에 들어갈




# for 변수 in 범위 : 

#     실행구문



# '''

#  1부터 10까지의 정수를 출력 (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) range는 범위를 나타냅니다 예시 range( 시작 , 끝값 , 단계)
#  if 1~n 까지의 정수라면 (1 , (n+1), 1)
# for num in range (1 , 11 , 1 ) :
#      print(f'{num}.hello')
#      print('hello')

#  0부터 10까지의 정수를 출력

# for num in range(0, 11 , 1):
#     print(f'num:{num}')

#range() 간략화 - 단계가 1인 경우 단계를 생략할 수 있다.

# for num in range(0,11):
#     print(f'num: {num}')

 #range() 간략화 - 단계가 생략되고 시작이 0이면 시작도 생략 가능하다.

# for num in range(11):
#     print(f'num: {num}')


#quiz) 2~8 사이의 짝수 출력하기

# for num in range(2, 42 ,2 ):
#     print(f'num: {num}')




# for num in range(1 , 16 ):
#     if 2 <= num <= 8 and num % 2 == 0:
#         print(num)


#Quiz) 사용자가 입력한 횟수만큼 '메일발송!' 문자열 출력하기
# count = int(input('횟수를 입력하세요 :'))
# for text in range(count):
#     print(f'[{text+1}]메일 발송 !')

#1~10사이의 정수를 출력하고 , 정수가 3의 배수이면 '3의 배수' 출력하기
# for num in range(1, 11 ):
#     if num % 3 == 0:
#         print(f'{num:2}: 3의 배수')
#     else:
#         print(f'{num:2}: 3의 배수가 아닙니다.')

# 사용자가  원하는 구구단을 입력하면 해당 구구단을 출력하자.
# googoo = int(input('원하는 구구단의 숫자를 입력하세요 :'))
# print(f'---{googoo}단 출력 ---')
# for num in range(1,10):
#     print(f' {googoo} X {num} = {googoo * num }')

# print('---값이 모두 출력되었습니다.---')



#quiz ) 1~ 10까지 정수의 합 출력하기

# Integer = 0

# for num in range(1, 11):
#     Integer += num
# print(f'1부터 10까지의 정수의 합은{Integer}입니다')


# result = sum(range(1, 11))
# print(f'합계: {result}')


# quiz) for문을 이용해서 1~100까지 정수 중에서 
# 3과 7의 공배수와 최소공배수를 출력하시오.
# min = True
# for i in range(1, 101):
#     if i % 3 == 0 and i % 7 == 0 and min == True:
#         print(f'{i}는 3과 7의 최소공배수입니다.')
#         min = False
#     elif i % 3 == 0 and i % 7 == 0 :
#         print(f'{i}는 3과 7의 공배수입니다.')
# minnum = 0
# for num in range(1, 101):
#     if num % 3 == 0 and num % 7 == 0:
#         print(f'3과 7의 공배수 : {num}')
#         if minnum ==0: minnum = num

# range () 함수 정리
# 단계가 1인경우에만 생략이 가능합니다. @range(1 , 10 , 1 )
# 단계가 생략이 되면 시작데이터도 생략 가능합니다 @range (5) = 0부터 4까지 1씩 단계가 늘어나는것입니다.

# 단계 감소란 @range(10,0,-1)이란 10부터 1까지 -1씩 감소하는것을 나타냅니다.
# for i in range(10,0,-1):
#     print(f'discount:{i}')     

# #문자열을 이용한 for문(****)
# '''
# 지금까지 이터러블에 range () 함수를 이용한 예를 살펴봤습니다.
# 그런데 이터러블에는 다음과 같이 문자열도 이용할수있습니다.
# '''

# for ch in 'hello':
#     print(f'ch : {ch}')

#quiz) 50보다 작은 7의 배수를 출력하는 프로그램을 만드세요.
# for num in range(7, 51):
#     if num  % 7 == 0:
#         print(f'7의배수는 : {num}이다.')


# while 문 : ~~ 하는 동안 ==> 조건에 의한 반복


# while True:
    # print('무한루프입니다 종료하려면 break를 입력하세요.')
    # ended = input('종료? (y/n) : ')
    # if ended == 'y':
        # print('종료합니다.')
        # break
    # else:
        # print('계속 실행중...')
# num = 1
# 
# while num <= 10:
    # print(f'num : {num}')
    # num += 1               # num = num + 1과 같은 표현입니다. 
                          #num에 1을 더한값을 다시 num에 저장하는것입니다. num += 1은 num = num + 1의 축약형입니다.



#quiz) while 문을 이용해서 구구단 전체 출력하기
# 
# dan = 2
# while dan <= 9:
    # print(f'---{dan}단---')
    # num = 1
    # while num <= 9:
        # print(f'{dan} x {num} = {dan * num:2}', end='\t')
        # num += 1
    # print(f"{dan}단이 모두 출력되었습니다.")
    # dan += 1
# quiz) while 문과  if 문을 이용해서 0~100까지의 정수 중 1과 0의 최소 공배수 출력하기
# 
# 
# num = 1
# minnum= 0
# while num <= 101:
# 
    # if num % 3 == 0 and num % 8 == 0:
        # print(f'3과 8의 공배수 : {num}')
        # if minnum == 0: 
        #    minnum = num
# 
# 
# 
# num += 1   
# 
# print(f'3과 8의 최소공배수 : {minnum}')

# 반복문 내 실행 제어 (continue, break, pass)
# continue : 반복문 내에서 continue를 만나면, continue 아래의 코드는 실행하지 않고, 다음 반복으로 넘어갑니다.)
# break : 반복문 내에서 break를 만나면, 반복문을 즉시 종료합니다.
# pass : 반복문 내에서 pass를 만나면, 아무런 동작도 하지 않고, 다음 줄로 넘어갑니다. 
# (보통은 코드 작성이 필요한 부분에 일시적으로 사용됩니다.)    

# continue : 반복문 내에서 continue를 만나면, continue 아래의 코드는 실행하지 않고, 다음 반복으로 넘어갑니다.)
# for num in range( 1, 11):
    # if num % 2 == 0:
        # continue 
    # print(f'num : {num}')  

# break : 반복문 내에서 break를 만나면, 반복문을 즉시 종료합니다.
# count = 1
# for num in range(1,11):
    # print(f'count : {num}')
    # count += 1  
    # if count > 10 :
        # print('반복문을 종료합니다.')
        # break
# for~esle 문 :
#(break문에 의해 중간에 종료되지 않았을 때 else문이 실행됩니다.) 
# 
# for num in range(1,6):
    # print(f'num : {num}')
# print('반복문을 종료')
# 

# pass : 반복문 내에서 pass를 만나면, 아무런 동작도 하지 않고, 다음 줄로 넘어갑니다.
# (보통은 코드 작성이 필요한 부분에 일시적으로 사용됩니다.)

# for num in range(1, 10):
    # pass
'''
삼각형의 넓이 구하기
가로와 세로 길이의 변화에 따른 삼각형의 넓이를 구하는 프로그램을 만들어보자.
단, 가로 길이는 1부터 2의 배수로 증가하고
세로길이는 1부터 3의 배수로 증가하며,
삼각형의 넓이가 150보다 크면 프로그램을 종료한다.
'''


# count = 1
# max_area = 150
# 
# while True:
    # result = (count *2) * (count * 3) / 2
    # print(f'삼각형의 넓이는 : {result}')
    # if result > max_area: break
        # 
    # count += 1
# 1부터 100까지 '홀수'의 합 구하기 (for문 사용)
# range() 함수의 단계(step) 인자를 활용하여 1부터 100 사이의 모든 홀수를 더하고 그 결과를 출력하세요.
# 
# 힌트: range(시작, 끝, 단계)를 이용해 홀수만 골라낼 수 있습니다.
# 
# sum = 0
# num = 0
# for num in range(1, 100, 2):
    # sum += num
# print(f'1부터 100까지 홀수의 합은 : {sum}')  #2500

# 숫자를 계속 입력받다가 0을 입력하면 종료 (while문 사용)
# 사용자에게 숫자를 입력받아 출력하는 과정을 반복합니다. 
# 단, 사용자가 숫자 0을 입력하면 "프로그램을 종료합니다"라는 메시지와 함께 반복문을 빠져나오세요.
# num = 0
# while True:
    # num = int(input('숫자를 입력하세요 (0 입력 시 종료) : '))
    # if num == 0:
        # print ('프로그램 종료')
        # break
    # else:
        # print(f'입력한숫자는 : {num}입니다.')
    # 
    #문제 3. 사각형의 넓이가 200을 넘을 때 종료 (while문 응용)
# 삼각형 문제와 비슷합니다. 아래 조건에 따라 사각형의 넓이를 출력하다가, 넓이가 200을 초과하면 멈추는 프로그램을 작성하세요.
# 
# 조건 1: 가로 길이는 2부터 시작하여 반복할 때마다 2씩 증가합니다. (2, 4, 6...)
# 
# 조건 2: 세로 길이는 1부터 시작하여 반복할 때마다 3씩 증가합니다. (1, 4, 7...)
# 
# 조건 3: 사각형의 넓이가 200보다 크면 break를 사용하여 종료합니다.

# count = 1
# max_area = 200
# w = 2
# h = 1
# 
# while True:
#  area = w * h 
#  print(f'{count}회차 사각형의 넓이는 : {area}')
#  if area > max_area:
    # print('사각형의 넓이가 200을 초과했습니다. 프로그램을 종료합니다.')
    # break
# 
# 
# 
# w += 2
# h += 3
# count += 1


#퀴즈: 저금통 시뮬레이션
# 당신은 매일 저금통에 돈을 넣기로 했습니다. 규칙은 다음과 같습니다.
# 
# 첫날(1일차)에는 100원을 넣습니다.
# 
# 다음 날부터는 전날 넣었던 금액보다 200원씩 더 많이 넣습니다. (즉, 2일차=300원, 3일차=500원...)
# 
# 저금통에 모인 전체 금액(총합)이 5,000원을 초과하면 저금을 중단합니다.

# insertcoin = 100
# date = 1
# putcoin = 200
# total = 0
# while True:
    # total += insertcoin
# 
    # print(f'{date}일차: {insertcoin}원을 넣었습니다. 총 금액: {total}원')
# 
    # if total > 5000:
        # print('총 금액이 5,000원을 초과했습니다. 저금을 중단합니다.')
        # break   
    # date += 1   
    # insertcoin += putcoin
# i = 10
# while i > 0:
    # print(i, end=' ')
    # i -= 3     
# 


# 정답: ( 여기에 답을 적어주세요 )

# sum = 0
# for i in range(1, 10):
    # sum += i
    # if sum > 10:
        # break
# print(sum)