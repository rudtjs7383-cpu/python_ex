#split

names = ('박찬호', '이승엽', '박세리', '박지성', '이순철', '선동열', '손흥민', '김연아')
print(f'names {names}')
print(f'namestype {type(names)}')


str = '박찬호 이승엽 박세리 박지성 이순철 선동열 손흥민 김연아'
splitedstr = str.split('+')                     #tuple이 아닌 , list로 나오게됨
print(f'splitedstr : {splitedstr}')
print(f'splitedstr : {type(splitedstr)})')


splitedstr= tuple(splitedstr)                   #다시 tuple로 바꾸고싶다면 tuple()함수를 
print(f'splitedstr : {splitedstr}')
print(f'splitedstr : {type(splitedstr)})')



member1 = ('이름/나이/전화번호/메일')
memsplit = member1.split('/')
print(f'이름은 :{member1[:2]}')