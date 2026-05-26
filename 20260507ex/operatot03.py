# 비교 연산자
# 비교 연산자는 두 값을 비교하고 그 결과가 참(true)인지 거짓(false)인지를 알려주는 연산자입니다.
#''''''
# a == b a와 b는 같다 = > True or False
# a != b a와  b는 같지않다. => True or False
# a > b a가 b보다 크다.=> True or False
# a >= b a가 b보다 크거나 같다
# a < b b가  a보다 크다
# a <= b b가 a보다 크거나 같다


# num1 = 10  
# num2 = 20

# num1 = 10; num2 = 20
# print(num1 == num2)
# print(num1 != num2)
# print(num1 > num2)
# print(num1 >= num2)
# print(num1 < num2)
# print (num1 <= num2)




#quiz) 범퍼카 탑승 가능 판별하기
# ''''''
# DW놀이동산에서 범퍼카는 신장이 120cm 이상인 어린이만 탑승할수 있습니다.
# 사용자가 신장을 입력하면 탑승할수있는지 여부를 출력하는 프로그램을 만들자

# height = int(input("어린이의 신장을 입력하세요"))
# print(height >= 120)


# #문자 vs 문자 비교
# print("a" == "b")          #False
# print("a"<"b")             #True
# print("a" > "b")           #False
# #이유는 아스키코드에 있습니다, 대문자는 소문자보다 더 작은수이며 예시를들었을때 대문자 A는 65 소문자 a는 97입니다.
# print(ord('c'))                    #해당 문자를 숫자로 볼수있는 함수 (ord를 입력했을때 나오는 c의 숫자는 99입니다.


# str1 = 'hello'
# str2 = 'hello'
# print(str1 == str2)
# print(str1 != str2)
# print (str1 > str2)
# print(str1  < str2)
# "---------------------------"

# str1 = 'hello'                         #532
# str2 = 'python'                        #674
# print(f'str1 != str2 : {str1 != str2}')
# print(ord('h'))
# print(ord('e'))
# print(ord('l'))
# print(ord('l'))
# print(ord('o'))
# print(ord('p'))
# print(ord('y'))
# print(ord('t'))
# print(ord('h'))
# print(ord('o'))
# print(ord('n'))
# print(f'hello의 총합은 {104 + 101 + 108 + 108 + 111}이다.')
# print(f'python의 총합은{112 + 121 + 116 + 104 + 111 +110}이다.')
# 그러므로 hello의 532 값과 python의 674 값은 같지않다에 True가 나타나게되는것입니다.
