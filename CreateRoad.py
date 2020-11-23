

BaseRoad=[1,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1]
NList=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

#모든 방향은 LED Matrix 출력 기준임(좌우가 바꿔어 있음)

def NR(NowRoad):
    return NowRoad

def R1(NowRoad):            #길전체가 오른쪽으로 이동
    if NowRoad[4]==1:       #벽에 붙었다면 실행X
        return NowRoad
    for i in NList:
        if NowRoad[i]==1:   
            NowRoad[i]=0
            NowRoad[i-1]=1  
    return NowRoad


def L1(NowRoad):            #길전체가 왼쪽으로 이동
    if NowRoad[19]==1:      #벽에 붙었다면 실행X
        return NowRoad
    for i in reversed(NList):
        if NowRoad[i]==1:
            NowRoad[i]=0
            NowRoad[i+1]=1
    return NowRoad

def LNar1(NowRoad):         #왼쪽 길이 한칸 줄어듬
    Nl=NowRoad[4:20]
    f1=Nl.index(1)
    e1=Nl[f1+1:].index(1)+f1
    if (e1-f1)<=2:          #길 사이가 두칸 이내라면 실행X
        return NowRoad
    for i in reversed(NList):
        if NowRoad[i]==1:
            NowRoad[i]=0
            NowRoad[i-1]=1
            return NowRoad

def RNar1(NowRoad):         #오른쪽 길이 한칸 줄어듬
    Nl=NowRoad[4:20]
    f1=Nl.index(1)
    e1=Nl[f1+1:].index(1)+f1
    if (e1-f1)<=2:          #길 사이가 두칸 이내라면 실행X
        return NowRoad
    for i in NList:
        if NowRoad[i]==1:
            NowRoad[i]=0
            NowRoad[i+1]=1
            return NowRoad

def RWid1(NowRoad):         #오른쪽 길이 한칸 늘어남
    if NowRoad[4]==1:       #벽에 붙어있다면 실행X
        return NowRoad
    for i in NList:
        if NowRoad[i]==1:
            NowRoad[i]=0
            NowRoad[i-1]=1
            return NowRoad

def LWid1(NowRoad):         #왼쪽 길이 한칸 늘어남
    if NowRoad[19]==1:      #벽에 붙어 있다면 실행X
        return NowRoad
    for i in reversed(NList):
        if NowRoad[i]==1:
            NowRoad[i]=0
            NowRoad[i+1]=1
            return NowRoad

def RptRoad(NowRoad,CR,n):  #한가지 함수를 n번 반복
    for i in range(n):
        CR(NowRoad)
        LookGood(NowRoad)   #출력 함수 변경 하기

def DRptRoad(NowRoad,CR1,CR2,n):    #두가지 함수를 n번 번갈아가며 반복
    for i in range(n):
        CR1(NowRoad)
        LookGood(NowRoad)
        CR2(NowRoad)
        LookGood(NowRoad)

def LookGood(NowRoad):      #화면에서 잘 보이게 하는 용도
    a=[]
    for i in range(24):
        if NowRoad[i]==1:
            a.append("■")
        else:
            a.append("□")
    print(a)


### 출력 예시

NowRoad=BaseRoad

RptRoad(NowRoad,NR,5)
DRptRoad(NowRoad,R1,NR,3)
DRptRoad(NowRoad,L1,NR,6)
RptRoad(NowRoad,RNar1,3)
RptRoad(NowRoad,R1,10)
RptRoad(NowRoad,NR,5)
RptRoad(NowRoad,NR,5)

