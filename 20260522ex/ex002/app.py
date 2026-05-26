import module01
import module02
import module03

if __name__ == '__main__':
 print('이 곳은 실행파일입니다.')
 
print(f'실행파일의 __name__: {__name__}')




#module01의 함수가 실행됩니다.      __name__은 파이썬에서 정의한 전역변수
# module의 __name__: module01
# module02의 함수가 실행됩니다.
# module의 __name__: module02
# module03의 함수가 실행됩니다.
# module의 __name__: module03
# 이 곳은 실행파일입니다.
# 실행파일의 __name__: __main__