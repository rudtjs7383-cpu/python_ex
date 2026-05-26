# 지금까지는 파이썬 셸 창에서 데이터를 출력하거나 입력했습니다. 
# 이 방법은 데이터를 일시적으로 메모리에 보관할뿐 영구적이지않습니다.
# 이번에는 문자열을 영구적인 보관방법으로 텍스트 파일을 다루는 방법에대해서 알아보겠습니다.
# 1단계는 파일열기 2단계는 쓰고/읽기 3단계는 파일닫기 입니다
# 1단계 > 파일을 열기위해서는 open()함수를 이용하고 파일열기에 성공하면 
#  파일은 객체로 만들어져 메모리에 생성됩니다 open()을 사용할때에 
# 어떤용도로 사용할것인지 지정해주는것이 좋습니다 읽기모드 'r' 쓰기모드 'w' 이어쓰기모드 'a'
# 2단계 > 객체에 문자열을 쓸때에는 write() 객체에 쓴 문자열을 읽을때는 read()를 사용합니다.

# file = open(r'C:\LKS\python_ex\test.txt','w',encoding= 'utf-8') #파일을 '쓰기'모드로 open한다.
# result = file.write('Hello python!')                 #쓰기 (write)
# print(f'result : {result}')
# file.close()                                 #파일 닫기  (close, 외부자원 해제)
# 

# file = open(r'C:\LKS\python_ex\test.txt','r')
# readResult = file.read()                               #읽기 (read)
# print(f'readResult : {readResult}')
# print(f'readResulttype : {type(readResult)}')
# 
# readResult = int(readResult)
# readResult += 1
# print(f'readResult : {readResult}')
# 
# file.close()
# 
file = open(r'C:\LKS\python_ex\test.txt','a')
file.write('\n hello~')
file.close()

file = open(r'C:\LKS\python_ex\test.txt','a')
file.write('\n hi~')
file.close()

with open (r'C:\LKS\python_ex\test.txt','a') as file:
    file.write('\n hello~')