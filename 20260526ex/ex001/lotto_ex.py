import random

userNums = []      # 내가 고른 번호 6개를 담을 주머니
randNums = []      # 컴퓨터가 무작위로 뽑은 로또 번호 6개를 담을 주머니
collect = []       # 내가 맞춘 번호들만 따로 모아둘 주머니


def setUNumbers(ns):
    global userNums    # setter > 어떠한 데이터를 세팅하는 함수 set+(UNumbers)
    userNums = ns   

def getUNumbers():      # getter > 어떠한 데이터를 가져오는 함수 get + (UNumbers)
    return userNums

def setRNumbers():
    global randNums

    randNums = random.sample(range(1,46),6)

def getRNumbers():
    return randNums


def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)

    return collect

