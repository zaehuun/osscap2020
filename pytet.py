from matrix import *
import LED_display as LMD
import threading
import random
import keyboard #sudo pip3 install keyboard
import time
load = [[ 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10 ],
        [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10 ],
        [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10 ],
        [ 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10 ]
         ]

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
            else:
                continue
        print()


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

arrayScreen = [[ 10, 10, 10, 10, 10, 10, 10, 10, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10, 10, 10, 10, 10, 10 ]] * 35

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

K = Key()
idx = 0
while True:
    K.key = ''
    time.sleep(0.2) 
    keyboard.hook(K.key_input)
    
    if K.key == 'q':
        print('Game terminated...')
        break
    elif K.key == 'a': # move left
        left += 1
    elif K.key == 'd': # move right
        left -= 1
 
           
    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(10):
        print("crush")
        break


        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    arrayScreen.pop(0)
    arrayScreen.append(load[idx])
    idx += 1
    if idx > 3:
        idx = 3
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