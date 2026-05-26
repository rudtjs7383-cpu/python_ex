#객체란 속성과 기능을 가지고있으며, 속성이란 사용자가 정의한 변수(입력한 변수)
#기능이란 사용자가 정의한 함수(만들어낸 함수)입니다.

#클래스(객체를 만들기 위한 툴(설계도)) 문법


#붕어빵 클래스
# class FishBread:            #클래스 선언
    #  속성(attribute)
    # def __init__(self, f, b):         #클래스 속성을 정의할때 __init__을 사용하는것은 일종의 약속이다.
        # self.flour = f                #self는 매개변수를 이용할때 사용합니다
        # self.bean = b
    # 기능 (function,method)
    # def makeFishBread(self):
        # print('붕어빵 제조')
# 
# 붕어빵 클래스로부터 객체를 만들어봅시다.(객체 생성)
# myFishBread = FishBread('팥','밀가루')   
# friendFishBread = FishBread('호박','쌀가루')
# hisFishBread = FishBread('꿀','밀가루')    
# print(f'내 붕어빵의 내용물: {myFishBread.flour}')
# print(f'내 붕어빵의 반죽: {myFishBread.bean}')
# 
# print(f'친구 붕어빵의 내용물: {friendFishBread.flour}')
# print(f'친구 붕어빵의 반죽: {friendFishBread.bean}')
# 
# print(f'옆집아저씨의 붕어빵의 내용물: {hisFishBread.flour}')
# print(f'옆집아저씨의 붕어빵의 반죽: {hisFishBread.bean}')
# 계산기 클래스

# class Calculator:
    # 속성
    # def __init__(self,n1,n2):
        # self.num1 = n1
        # self.num2 = n2
    # 기능         
    # def add(self):
    #  print(f'add :{self.n1 + self.n2}')
    # def sub(self):
    #  print(f'sub :{self.n1 - self.n2}')
    # def mul(self):
    #  print(f'mul :{self.n1 * self.n2}')
    # def div(self):
    #  print(f'div :{self.n1 / self.n2}')
# myCalculator = Calculator(10,20)
# friendCalculator = Calculator(100,200)
# myCalculator.add()
# myCalculator.sub()
# myCalculator.mul()
# myCalculator.div
# 
# friendCalculator.add()
# friendCalculator.sub()
# friendCalculator.mul()
# friendCalculator.div()




# class Print:
#    def __init__(self,print):
    #   pass     
     
# 인간 클래스 만들기
# class Human:
#    속성
    # def __init__(self,height,weight):
    #    self.height = height
    #    self.wegiht = weight
    #    
#    기능
    # def walk (self):
    #    print('걷자!')
# 
    # def run(self):
    #    print('뛰자!')
# 
    # def printMyInfo(self):
    #    print(f'나의 신장 : {self.height}')
    #    print(f'나의 체중 : {self.weight}')       
# 
# 
# 
# human1 = Human(183,87)     
# human2 = Human(165,49)    
# 
# human1.printMyInfo()
# human2.printMyInfo()
# 
# human1 = human2
# human1.printMyInfo()
# 
# human1.height = 200
# human1.wegiht = 39
# 
# human2.printMyInfo()
# 다음 실행결과를 참고하여 컴퓨터와 함께하는 가위바위보 프로그램을 만들기입니다
# 난수를 이용해서 게임을 진행하고 결과를 출력해봅시다.

# import random
# rspData ={1:'가위', 2:'바위', 3:'보'}
# 
# mySelectNum = int(input('숫자를 선택하세요 (1.가위 2.바위 3.보)'))
# comSelectNum = random.randint(1,3)
# 
# print(f'유저가 낸 것 : {rspData[mySelectNum]}')
# print(f'컴퓨터가 낸 것 : {rspData[comSelectNum]}')
# 
# if mySelectNum == comSelectNum:
    # print('유저와 컴퓨터가 무승부입니다')
# 
# elif (
    # (mySelectNum ==1 and comSelectNum ==3)
    # or (mySelectNum == 2 and comSelectNum == 1 )
    # or (mySelectNum == 3 and comSelectNum == 2)
    # ):
    # print('유저가 승리하였습니다! 승리!')
# 
# else:
    # print('컴퓨터가 승리하였습니다! 패배!')



# 다음 실행결과를 참고하여 단어장에서 무작위로 출력되는 영어단어를 맞추는 프로그램을 만드시오
# 영어 = {football ,pencil,eraser,piano,guitar,doll,car,clock}
# 한글 = {축구,연필,지우개,피아노,기타,인형,자동차,시계}

# import random
# 
# wordDict = {
    # 'football':'축구',
    # 'pencil':'연필',
    # 'eraser':'지우개',
    # 'piano':'피아노',
    # 'guitar':'기타',
    # 'doll':'인형',
    # 'car':'자동차',
    # 'clock':'시계'
# }
# 
# engilshWords = list(wordDict.keys()) 
# 
# print('영단어의 한글을 맞춰보자!')
# 
# while True:
    # 
    # quizWord = random.choice(engilshWords)
    # correctAnswer = wordDict[quizWord]
# 
    # userAnswer = input(f'\n{quizWord}의 뜻은 무엇? ')
# 
    # if userAnswer == correctAnswer:
        # print('정답입니다. 똑똑하네요')
        # 
    # else:
        # print('정말로 그게 맞아요? 더 공부하세요!!')

# 다음의 요구되는 기능을 가진 mp3플레이어 모듈을 만들어보세요
# 곡추가,곡제거, 곡리스트 출력,일반재생모드,셔플재생모드
#곡의 목록에는 Dynamite.mp3 다시여기바닷가.mp3 마리아(maria).mp3 
#  When we disco.mp3  How You Like That.mp3 눈누난나.mp3 그 여름을틀어줘.mp3 가 있다
# 아리랑~.mp3 를 추가하고 제거 했다는것을 출력할수있는 코드를 만들어보자

# import random
# 
# class MP3Player:
    # def __init__(self):
        # self.Playlist = [
            # 'Dynamite.mp3',
            # '다시여기바닷가.mp3',
            # '마리아(maria).mp3',
            # 'When we disco.mp3',
            # 'How You Like That.mp3',
            # '눈누난나.mp3',
            # '그 여름을틀어줘.mp3'
        # ]
# 
    # 
    # def show_playlist(self):
        # print("\n=== 현재 플레이리스트 ===")
        # for i, song in enumerate(self.Playlist, 1):
            # print(f"{i}. {song}")
        # print("=======================\n")
# 
    # def addSong(self, song_name):
        # self.Playlist.append(song_name)
        # print(f' 곡을 추가합니다: {song_name}가 추가되었습니다.')
# 
    # def removeSong(self, song_name):
        # if song_name in self.Playlist:
            # self.Playlist.remove(song_name)
            # print(f' 곡을 제거합니다: {song_name}이 제거되었습니다.')
# 
    # def play_normalMode(self):
        # print(f'\n 순차적 재생모드입니다.')
        # for song in self.Playlist:
            # print(f' 현재 재생중 : {song}')
        # print(' 모든 곡의 재생이 완료되었습니다.\n')
# 
    # def play_shuffleMode(self):
        # print(f'\n 랜덤재생 모드입니다.')
        # 
        # shuffleList = self.Playlist.copy()
        # random.shuffle(shuffleList)
# 
        # for song in shuffleList:
            # print(f' 현재 재생중 : {song}')
        # print(' 모든 곡의 재생이 완료되었습니다.\n')
# 
# 
# 
# if __name__ == "__main__":
    # my_mp3 = MP3Player()
# 
    # 
    # my_mp3.show_playlist()
# 
    # 
    # my_mp3.addSong('아리랑~.mp3')
    # my_mp3.show_playlist()
# 
#    
    # my_mp3.play_normalMode()   # 일반 재생
    # my_mp3.play_shuffleMode()  # 셔플 재생
# 
#    
    # my_mp3.removeSong("아리랑~.mp3")
    # my_mp3.show_playlist()

# 가로가 32m,세로가 48m인 직사각형의 밭을 똑같은 크기의 정사각형으로 분할하여 나누어 주려고 한다.
# 정사각형의 크기를 가장 크게 했을 때 정사각형의 넓이를 구하는 모듈을 만드세요.

#정사각형 한 변의 길이 : 16m
#정사각형 한개 면적 256m(제곱)
#정사각형 개수 6.0개

import math

def calculate_max_square(width, height):

    
    
    side_length = math.gcd(width, height)
    
    
    area = side_length ** 2
    
   
   
    count = (width // side_length) * (height // side_length)
    
    return {
        "side_length": side_length,
        "area": area,
        "count": count
    }


if __name__ == "__main__":
   
    width = 32
    height = 48
    
    result = calculate_max_square(width, height)
    
    print(f"# 정사각형 한 변의 길이 : {result['side_length']}m")
    print(f"# 정사각형 한개 면적 : {result['area']}m²")
    print(f"# 정사각형 개수 : {result['count']}개")








































