from pytet import *
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