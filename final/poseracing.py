from flask import Flask, render_template, redirect, url_for

import threading as TH
app = Flask(__name__, static_url_path='/static') 


from matrix import *
import LED_display as LMD
import threading
import random
import keyboard #sudo pip3 install keyboard
import time
import copy
import os






crush = False

direct = None
@app.route("/") 
@app.route('/index')
def home():
    return render_template('tm.html')

@app.route("/center") 
def center():
    global direct
    direct = "center"
    if crush:
        os.system('exit')
    return "hello"

@app.route("/right") 
def right():
    global direct
    direct = "right"
    if crush:
        os.system('exit')
    return "hello"

@app.route("/left") 
def left():
    global direct
    direct = "left"
    if crush:
        os.system('exit')
    return "hello"

def LED_init1():
    global direct
    thread1=TH.Thread(target=main1, args=())
    thread1.setDaemon(True)
    thread1.start()
    return




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
    if (e1-f1)<=6:          #길 사이가 두칸 이내라면 실행X
        return NowRoad
    for i in reversed(NList):
        if NowRoad[i]==0:
            NowRoad[i]=10
            return NowRoad

def RNar1():         #오른쪽 길이 한칸 줄어듬
    Nl=NowRoad[4:20]
    f1=Nl.index(0)
    e1=Nl[f1+1:].index(10)+f1+1
    if (e1-f1)<=6:          #길 사이가 두칸 이내라면 실행X
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

def MakeP():
        Nt=NowRoad[4:20]
        f1=Nt.index(0)
        e1=Nt[f1+1:].index(10)+f1+1
        
        tmp = copy.deepcopy(NowRoad)
        #tmp[f1+(e1-f1)//2+4] = 5
        tmp[random.randint(f1+4,e1+3)] = 5
        road.append(tmp)


    

road = []
score = 0





def LED_init():
    thread=threading.Thread(target=LMD.main, args=())
    thread.setDaemon(True)
    thread.start()
    return

score = 0
def draw_matrix(m):
    global score
    
    array = m.get_array()
    for y in range(m.get_dy()-4):
        for x in range(4, m.get_dx()-4):
            if array[y][x] == 0:
                LMD.set_pixel(y, 19-x, 0)
            elif array[y][x] == 10:
                if score < 10:
                    LMD.set_pixel(y, 19-x, 2)
                elif score < 20:
                    LMD.set_pixel(y, 19-x, 6)
                elif score < 30:
                    LMD.set_pixel(y, 19-x, 4)
                elif score < 40:
                    LMD.set_pixel(y, 19-x, 3)
                else:
                    LMD.set_pixel(y, 19-x, 7)
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
            
def times():
    if score < 10:
        return 0.5
    elif score <20:
        return 0.4
    elif score <30:
        return 0.3
    elif score <40:
        return 0.2
    else:
        return 0.1


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
iScreenDy = 32
iScreenDx = 16
iScreenDw = 4
top = 3
left = iScreenDw + iScreenDx//2 - 1

newBlockNeeded = False
def WhenCrush():
    Carray=arrayScreen[:37]
    iCarray=Matrix(Carray)
    oCarray=Matrix(iCarray)
    draw_matrix(oCarray)
    time.sleep(0.5)

    for i in range(len(Carray)):
        for j in range(len(Carray[0])):
            if (Carray[i][j]==5) or (Carray[i][j]==1):
                Carray[i][j]=0
    for i in range(11):
        for j in range(len(Carray)):            
            f0=Carray[j].index(0)
            if 10 in Carray[j][f0+1:]:
                e1=Carray[j][f0+1:].index(10)+f0+1
                Carray[j][e1]=0
            Carray[j][f0-1]=0
            
        iCarray=Matrix(Carray)
        oCarray=Matrix(iCarray)
        draw_matrix(oCarray)
        time.sleep(times())
arrayScreen = [[ 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10 ]] * 36
NList=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
NowRoad=[10,10,10,10,10,10,10,10,0,0,0,0,0,0,0,0,10,10,10,10,10,10,10,10]
#def main(a):

st = time.time()
def main1():
    global left, top, NowRoad, direct, st,score
    
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
    

    idx = 0
    flag = False
    realscore = 0
    cntp = 0
    while True:
        print("time :",time.time() - st)
        print("score : ", realscore)
        print(direct)

        time.sleep(times()) 
 
        rand = random.randint(0,5)
        if flag:
            rand = random.randint(0,4)
            flag = False
        
        if direct == 'center':
            pass
        elif direct == 'left': # move left
            left += 1
            direct = 'center'
        elif direct == 'right': # move right
            left -= 1
            direct = 'center'
    
        if len(road) < 6:

        
            if rand == 0:
                RptRoad(RNar1,3)
                DRptRoad(NR,R1,4)
                DRptRoad(NR,L1,7)
            elif rand == 1:
                RptRoad(LNar1,3)
                DRptRoad(NR,L1,3)
                DRptRoad(NR,R1,6)
            elif rand == 2:
                DRptRoad(NR,R1,5)
                DRptRoad(NR,L1,5)
            elif rand == 3:
                RptRoad(RWid1,5)
                RptRoad(LNar1,3)
            elif rand == 4:
                RptRoad(LWid1,4)
                RptRoad(RNar1,2)


            elif rand == 5:
                flag = True
                #print("item")
                MakeP()

           
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

        if tempBlk.anyGreaterThan(10):
            print("crush")
            print("score : ", realscore + cntp * 50)
            WhenCrush()
            crush = True
            break
    
        if tempBlk.getItem(6):
            cntp += 1
            for i in range(3,6):
                for j in range(24):
                    if arrayScreen[i][j] == 5:
                        arrayScreen[i][j] = 0
                        break
            

                
        
        arrayScreen.pop(0)
    #arrayScreen.append(road[idx])
        arrayScreen.append(road.pop(0))

    
    
    #idx += 1
    #if idx >= len(road):
    #    idx = 0
    
        score = time.time() - st
        realscore = (time.time()-st) * 10
        iScreen = Matrix(arrayScreen)
        oScreen = Matrix(iScreen)
        currBlk = Matrix(arrayBlk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); 
        os.system('clear') 

### end of the loop
###
    


if __name__ == "__main__":
    LED_init1()
    app.run()

