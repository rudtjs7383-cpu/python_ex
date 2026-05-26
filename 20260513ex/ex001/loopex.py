#quiz ) 369게임 만들기
# '''
# 친구들끼리 많이 하는 369 게임을 만들어봅시다.
# 1부터 99까지 1씩 증가하면서 숫자에 3,6,9가 들어있을때마다 숫자와 함께
# '짝!'을 출력합니다.
# 33 -> 짝짝!
# 6 -> 짝!
# 99 -> 짝짝!
# '''

# for num in range(1, 100):
# 
    # if num <= 9:                # 1의 단위
        # if num % 3 == 0:
            # print(f'{num}, 짝!')
            # print(num, ', 짝!', end='')
        # else:
            # print(num, end='')
    # else:                       # 10의 단위 
        # print(f'{num}')       # 12 > 1, 2 : 16 > 1, 6 : 99 > 9, 9
        # printStr = str(num)
        # print(num, end='')
# 
        # firstNum = num // 10    # 15 > 15 // 10 -> 1
        # secondNum = num % 10    # 15 > 15 % 10  -> 5, 30 > 0
# 
        # if firstNum % 3 == 0:
            # print(f'짝!')
            # printStr += ', 짝!'
            # print(', 짝!', end='')
# 
        # if secondNum % 3 == 0 and secondNum != 0:
            # print(f'짝!')
            # printStr += ', 짝!'
            # print(', 짝!', end='')
        # 
    # print()

'''
대전역에는 3개 노선의 열차가 오전 9시부터 오후 6시까지 교차 운행한다.
3대의 열차가 교차하는 시간을 구해 열차 충돌사고를 막으세요.
(단 매일 오전 9시에 대전역에서 모든 열차가 출발한다.)
------------------------------------------------
A호차: 첫차 오전 9시 | 마지막차 오후 6시 | 운행간격 10분
B호차: 첫차 오전 9시 | 마지막차 오후 6시 | 운행간격 25분
C호차: 첫차 오전 9시 | 마지막차 오후 6시 | 운행간격 30분

''' 
# trainA = 10
# trainB = 25
# trainC = 30
# 
# for n in range(1, 541):
#  if n % trainB == 0 and n % trainC == 0 and n % trainA == 0:
#   print('trainB <-> trainC <->trainA')
#   print(9 + n/ 60 ,end= '')       #시
#   print('시' , end= '')
#   print(n % 60 , end= '')         #분
#   print('분')
#    print(f'{9 + n //60}시{n % 60}분')

    # if n % trainA == 0 and n % trainB == 0:
        # print('trainA <-> trainB')
        # print(9 + n/ 60 ,end= '')       #시
        # print('시' , end= '')
        # print(n % 60 , end= '')         #분
        # print('분')
        # print(f'{9 + n //60}시{n % 60}분')

    # elif n % trainB == 0 and n % trainC == 0:
    #  print('trainB <-> trainC')
    #  print(9 + n/ 60 ,end= '')       #시
    #  print('시' , end= '')
    #  print(n % 60 , end= '')         #분
    #  print('분')
    #  print(f'{9 + n //60}시{n % 60}분') 

    # elif n % trainC == 0 and n % trainA == 0:
    #  print('trainC <-> trainA')
    #  print(9 + n/ 60 ,end= '')       #시
    #  print('시' , end= '')
    #  print(n % 60 , end= '')         #분
    #  print('분')
    #  print(f'{9 + n //60}시{n % 60}분')


    # if n % trainB == 0 and n % trainC == 0 and n % trainA == 0:
    #  print('trainB <-> trainC <->trainA')
    #  print(9 + n/ 60 ,end= '')       #시
    #  print('시' , end= '')
    #  print(n % 60 , end= '')         #분
    #  print('분')
      #print(f'{9 + n // 60}시 {'00' if n % 60 == 0 else str(n % 60)}분')

#quiz ) 로그인 기능 만들기
# '''
# 시스템 관리자 (administratot) 로그인 기능을 만들어봅시다.
# 관리자가 암호를 입력하고 로그인을 시도할 때 암호가 틀렸다면'암호를 다시 확인하세요' 를 츨력하고
# 다시 암호를 물어봅니다.
# 5회 이상 로그인에 실패하면 '로그인 실패 횟수 초과 !!' 메세지를 출력하고 종료합니다.
# 암호가 올바르다면 '로그인 됐습니다.' 를 출력하고 종료합니다. 올바른 암호는 'dwac1234'입니다.
# 
# '''
# ADMINPASSWORD = 'dwac1234'
# count = 1
# while True:
# 
    # if count >= 5:
        # print('로그인 실패')
        # break
# 
    # inputpwd = input('관리자 암호를 입력하세요 :')
    # 
# if inputpwd != ADMINPASSWORD:
    # print('X---> 암호를 다시 확인하세요.')
    # count += 1
# else:
#  inputpwd == ADMINPASSWORD
# print('O---> 로그인 됐습니다.')  
#  break

# quiz) 팩토리얼 만들기
# '''
# 사용자가 입력한 양수를 이용해 팩토리얼 값을 구하는 프로그램을 만드시오.
# 팩토리얼(factorial, !) n!은 1부터 양의 정수 n까지의 모든 정수를 곱한 값을 말한다.
# (예를 들어, 4!은 1x2x3x4 = 24이다.)
# '''  
# userinputintdata = int(input('양수 입력 :'))
# result = 1
# 
# for num in range (1, userinputintdata + 1):
    # result *= num
    # print(f'{userinputintdata}의 팩토리얼은 {result}이다.')
# quiz) 숫자 맞추기 게임을 만들자
'''
0부터 100사이의 난수를 발생시키고 사용자가 난수를 맞힐 때까지 계속해서 물어보는 게임을 만드시오. 
다음은 프로그램 개발에 필요한 요구사항이다.
--- 요구사항 ---
- 1부터 100까지의 난수를 발생시킨다.
- 사용자가 입력한 숫자가 난수와 일치하면 ‘정답입니다.’를 출력하고 게임을 종료한다.
- 사용자가 입력한 숫자가 난수와 일치하지 않으면 ‘틀렸습니다. 다시 입력하세요.’를 출력하고, 다시 물어본다.
- 기회는 10회로 제한한다. 만약 열 번을 넘어가면 ‘게임에 졌습니다.’를 출력하고 게임을 종료한다.
- 사용자가 틀릴 때마다 사용자가 입력한 숫자와 난수를 비교해서 크고, 작음을 출력한다. 
- 게임이 종료하기 전 난수를 출력한다. 
'''
# import random
# 
# 
# target_number = random.randint(1, 100)
# count = 0
# chance = 10
# 
# print("--- 숫자 맞히기 게임을 시작합니다! (1~100) ---")
# 
# while count < chance:
    # count += 1
#    
    # try:
        # userinput = int(input(f"[{count}회차] 숫자를 입력하세요: "))
    # except ValueError:
        # print("숫자만 입력 가능합니다. 기회 1회를 사용하셨습니다.")
        # continue
# 
    # 
    # if userinput == target_number:
        # print(f"O---> {userinput}: 정답입니다!")
        # break
    # else:
        # print("X---> 틀렸습니다. 다시 입력하세요.")
        # 
        # 
        # if userinput > target_number:
            # print("힌트: 입력한 숫자보다 작습니다. ↓")
        # else:
            # print("힌트: 입력한 숫자보다 큽니다. ↑")
# 
# 
# if count >= chance and userinput != target_number:
    # print("\n기회를 모두 사용하셨습니다. 게임에서 졌습니다. ")
# 


#  로또프로그램을 만들어보자.

# import random
# 
# lotto_num = random.sample(range(1,46),6) 
# user_lotto = []
# lotto_num.sort
# 
# while len(user_lotto) < 6:
    # try:
    # 
        # num = int(input(f"{len(user_lotto) + 1}번째 번호: "))
        # 
        # 
        # if num < 1 or num > 45:
            # print("X---> 1부터 45 사이의 숫자만 입력 가능합니다.")
        # 
        # elif num in user_lotto:
            # print("X---> 이미 입력하신 번호입니다. 다른 숫자를 고르세요.")
        # 
        # else:
            # user_lotto.append(num)
            # 
    # except ValueError:
        # print("X---> 숫자만 입력해 주세요!")
# 
# 
# user_lotto.sort()
# print(f"\n 당신이 선택한 번호는: {user_lotto}")
# 
# 
# 
# print(f'이번주의 예상 로또번호는 {lotto_num}입니다')

# try:
#  num = int(input('숫자만 입력하세요:'))
# except ValueError:
    # print('그것은 숫자가 아닙니다')
# try와 except 는 붙어다니는 존재입니다
# try의 불록에는 사고가 날것같은 코드를 넣고
# except의 블록에는 사고가났으니 조치를 취할 코드를 넣습니다.

#ex) try: 를 입력한 후 엔터, 연산자를 입력후 에러가 날수도있다 라는 가정하에 
#except를 입력하여 조치를 취하는 것입니다.
# try:
#  print('계산을 시작합니다')
#  result = 10 / 0        #<----- 0으로 나누기는 불가능하기때문에 에러가 뜰것입니다.

# except:
#  print('그것은 나눌수없습니다')

# quiz) 다음 요구조건을 참고하여 가로와 세로 길이의 변화에 따른 사각형의 넓이를 구하는 프로그램을 만드시오.
'''
 - 가로 길이는 1부터 2의 배수로 증가한다. [1,2,4,6,8,10,12 ....]
 - 세로 길이는 1부터 3의 배수로 증가한다. [1,3,6,9,12,.....]
 - 사각형의 넓이가 150 보다 크면 프로그램을 종료한다. 
 - 가장 작은 사각형과 가장 큰 사각형의 넓이를 출력한다.
'''
width = 1
height = 1
count = 0
minarea = 0
last_area = 0 
max_limit = 150 

while True:
    currentarea = width * height
    
    
    if currentarea > max_limit: 
        break
    print(f'가로 : {width}, 세로 : {height}, 넓이 : {currentarea}')
    
    
    if count == 0:
        minarea = currentarea 
    
    last_area = currentarea 
    
    if width == 1:
        width += 1
    else: 
        width += 2

    
    if height == 1:
        height += 2
    else: 
        height += 3

    count += 1

print(f"가장 작은 넓이: {minarea}")
print(f"가장 큰 넓이: {last_area}")























  

















