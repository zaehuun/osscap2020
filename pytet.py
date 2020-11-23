
from matrix import *
import LED_display as LMD
import threading
import random
import keyboard #sudo pip3 install keyboard
import time
import copy


NowRoad=[10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,10,10,10,10,10,10,10,10]
NList=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

#모든 방향은 LED Matrix 출력 기준임(좌우가 바꿔어 있음)

def NR():
    return NowRoad

def R1():            #길전체가 오른쪽으로 이동
    if NowRoad[5]==0:       #벽에 붙었다면 실행X
        return NowRoad
    for i in NList:
        if NowRoad[i]==0:   
            NowRoad[i-1]=0 
            break
    for i in reversed(NList):
        if NowRoad[i]==0:   
            NowRoad[i]=10 
            break
    return NowRoad


def L1():            #길전체가 왼쪽으로 이동
    if NowRoad[18]==0:      #벽에 붙었다면 실행X
        return NowRoad
    for i in NList:
        if NowRoad[i]==0:   
            NowRoad[i]=10 
            break
    for i in reversed(NList):
        if NowRoad[i]==0:   
            NowRoad[i+1]=0 
            break
    return NowRoad


def LNar1():         #왼쪽 길이 한칸 줄어듬
    Nl=NowRoad[4:20]
    f1=Nl.index(0)
    e1=Nl[f1+1:].index(10)+f1+1
    if (e1-f1)<=5:          #길 사이가 두칸 이내라면 실행X
        return NowRoad
    for i in reversed(NList):
        if NowRoad[i]==0:
            NowRoad[i]=10
            return NowRoad

def RNar1():         #오른쪽 길이 한칸 줄어듬
    Nl=NowRoad[4:20]
    f1=Nl.index(0)
    e1=Nl[f1+1:].index(10)+f1+1
    if (e1-f1)<=5:          #길 사이가 두칸 이내라면 실행X
        return NowRoad
    for i in NList:
        if NowRoad[i]==0:
            NowRoad[i]=10
            return NowRoad

def RWid1():         #오른쪽 길이 한칸 늘어남
    if NowRoad[5]==0:       #벽에 붙어있다면 실행X
        return NowRoad
    for i in NList:
        if NowRoad[i]==0:
            NowRoad[i-1]=0
            return NowRoad

def LWid1():         #왼쪽 길이 한칸 늘어남
    if NowRoad[18]==0:      #벽에 붙어 있다면 실행X
        return NowRoad
    for i in reversed(NList):
        if NowRoad[i]==0:
            NowRoad[i+1]=0
            return NowRoad

def RptRoad(CR,n):  #한가지 함수를 n번 반복
    for i in range(n):
        road.append(copy.deepcopy(CR()))
    
   #출력 함수 변경 하기

def DRptRoad(CR1,CR2,n):    #두가지 함수를 n번 번갈아가며 반복
    for i in range(n):
        #road.append()  
        road.append(copy.deepcopy(CR1()))
        
        road.append(copy.deepcopy(CR2()))
  #      LookGood(NowRoad)

'''
def LookGood(NowRoad):      #화면에서 잘 보이게 하는 용도
    a=[]
    for i in range(24):
        if NowRoad[i]==10:
            a.append("■")
        else:
            a.append("□")
    print(a)
'''
### 출력 예시




road = []



RptRoad(R1,3)
RptRoad(L1,3)
RptRoad(RNar1,5)
RptRoad(RWid1,5)
print(len(road))
class Key :

    def __init__(self) :
        self.key = ''
    
    def key_input(self, e) :
        for code in keyboard._pressed_events :

            if code == 30 :
                self.key = 'a'
            elif code == 32 :
                self.key = 'd'
            elif code == 16 :
                self.key = 'q'

def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

#빨 1
#초 2
#노 3
#파 4
#핑 5
#민 6
#흰 7
def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()-4):
        for x in range(4, m.get_dx()-4):
            if array[y][x] == 0:
                LMD.set_pixel(y, 19-x, 0)
            elif array[y][x] == 10:
                LMD.set_pixel(y, 19-x, 4)
            elif array[y][x] == 2:
                LMD.set_pixel(y, 19-x, 2)
            elif array[y][x] == 3:
                LMD.set_pixel(y, 19-x, 3)
            elif array[y][x] == 1:
                LMD.set_pixel(y, 19-x, 1)
            elif array[y][x] == 7:
                LMD.set_pixel(y, 19-x, 7)
            elif array[y][x] == 5:
                LMD.set_pixel(y, 19-x, 5)
            else:
                continue



###
### initialize variables
###     

cntarr = [

    
        [[0,2,0],
        [0,2,0],
        [0,2,0],
        [0,2,0],
        [0,2,0]],
        
        [[3,3,3],
        [0,0,3],
        [3,3,3],
        [3,0,0],
        [3,3,3]],
        
        
        
        [[1,1,1],
        [1,0,0],
        [1,1,1],
        [1,0,0],
        [1,1,1]],]
cnttop = 18

####################################
arrayBlk = [[1,1,0],
            [1,1,0],
            [1,1,0]]


### integer variables: must always be integer!


iScreenDy = 32
iScreenDx = 16
iScreenDw = 4
top = 3
left = iScreenDw + iScreenDx//2 - 1

newBlockNeeded = False

arrayScreen = [[ 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10 ]] * 36

###
### prepare the initial screen output
###  

iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
LED_init()
draw_matrix(oScreen);

cnt = 3
while cnt:
    
    currBlk = Matrix(cntarr[cnt-1])
    tempBlk = iScreen.clip(cnttop, left, cnttop+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, cnttop, left)
    draw_matrix(oScreen);
    cnt -= 1
    time.sleep(1)
    
    

###
### execute the loop
###
st = time.time()
K = Key()
idx = 0
flag = False
while True:
    K.key = ''
    time.sleep(0.1) 
    keyboard.hook(K.key_input)
    
    rand = random.randint(0,4)
    if flag:
        rand = random.randint(0,3)
        flag = False
        
    if K.key == 'q':
        print('Game terminated...')
        break
    elif K.key == 'a': # move left
        left += 1
    elif K.key == 'd': # move right
        left -= 1
    
    if rand == 0:
        '''
        RptRoad(L1,3)
        RptRoad(R1,3)
        RptRoad(RNar1,5)
        RptRoad(RWid1,5)'''
        DRptRoad(NR,R1,3)
        DRptRoad(NR,L1,3)
    elif rand == 1:
        '''
        RptRoad(R1,3)
        RptRoad(L1,3)
        RptRoad(R1,3)
        RptRoad(L1,3)'''
        DRptRoad(NR,L1,5)
        DRptRoad(NR,R1,5)
    elif rand == 2:
        RptRoad(RNar1,3)
        DRptRoad(NR,R1,10)
        DRptRoad(NR,L1,10)
        DRptRoad(NR,R1,3)
        RptRoad(RWid1,3)
    elif rand == 3:
        RptRoad(RWid1,5)
        RptRoad(RNar1,5)
    elif rand == 4:
        flag = True
        print("item")
        Nt=NowRoad[4:20]
        f1=Nt.index(0)
        e1=Nt[f1+1:].index(10)+f1+1
        tmp = copy.deepcopy(NowRoad)
        tmp[f1+(e1-f1)//2+4] = 5
        road.append(tmp)
        
           
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(10):
        print("crush")
        print("score : ", time.time() - st)
        break
    
    if tempBlk.getItem(6):
        item_idx = road[idx-1].index(5)
        tempBlk[idx][item_idx] = 0
        print("get Item")
        
    arrayScreen.pop(0)
    arrayScreen.append(road[idx])

    
    
    idx += 1
    if idx >= len(road):
        idx = 0
    iScreen = Matrix(arrayScreen)
    oScreen = Matrix(iScreen)
    currBlk = Matrix(arrayBlk)
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); 

    
        
###
### end of the loop
###
    
