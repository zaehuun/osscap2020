class Matrix:
    count = 0

    def get_count(self):
        return Matrix.count
    
    def get_dy(self):
        return self._dy

    def get_dx(self):
        return self._dx

    def get_array(self):
        return self._array

    def __alloc(self, cy, cx):
        if cy < 0 or cx < 0:
            raise MatrixError("wrong matrix size")
        self._dy = cy
        self._dx = cx
        self._array = [[0]*self._dx for i in range(self._dy)]
        
    def __init__(self, arg):
        Matrix.count += 1
        if isinstance(arg, list):
            array = arg
            cy = len(array)
            cx = len(array[0])
            self.__alloc(cy, cx)
            for y in range(cy):
                for x in range(cx):
                    self._array[y][x] = array[y][x]
            return
        elif isinstance(arg, Matrix):
            other = arg
            cy = other._dy
            cx = other._dx
            self.__alloc(cy, cx)
            for y in range(cy):
                for x in range(cx):
                    self._array[y][x] = other._array[y][x]
            return
        else:
            self.__alloc(0, 0)
            return

    def __str__(self):
        return 'Matrix(%d, %d)' % (self._dy, self._dx)

    def print(self):
        print('[', end=' ')
        for y in range(self._dy-1):
            print('[', end=' ')
            for x in range(self._dx-1):
                print(self._array[y][x], end=', ')
            print(self._array[y][self._dx-1], end=' ')
            print('],') # , end=' ')
        print('[', end=' ')
        for x in range(self._dx-1):
            print(self._array[self._dy-1][x], end=', ')
        print(self._array[self._dy-1][self._dx-1], end=' ')
        print(']') # , end=' ')
        print(']')        

    def clip(self, top, left, bottom, right):
        cy = bottom - top
        cx = right - left
        temp = [[0]*cx for i in range(cy)]       
        for y in range(cy):
            for x in range(cx):
                if (top+y >= 0) and (left+x >= 0) \
                   and (top+y < self._dy) and (left+x < self._dx):
                    temp[y][x] = self._array[top+y][left+x]
                else:
                    raise MatrixError("invalid matrix range")
        return Matrix(temp)

    def paste(self, other, top, left):
        for y in range(other._dy):
            for x in range(other._dx):
                if (top+y >= 0) and (left+x >= 0) \
                   and (top+y < self._dy) and (left+x < self._dx):
                    self._array[top+y][left+x] = other._array[y][x]
                else:
                    raise MatrixError("invalid matrix range")

    def __add__(self, other):
        if (self._dx != other._dx) or (self._dy != other._dy):
            raise MatrixError("matrix sizes mismatch")
        temp = [[0]*self._dx for i in range(self._dy)]
        for y in range(self._dy):
            for x in range(self._dx):
                temp[y][x] = self._array[y][x] + other._array[y][x]                
        return Matrix(temp)

    def sum(self):
        total = 0
        for y in range(self._dy):
            for x in range(self._dx):
                total += self._array[y][x]
        return total

    def mulc(self, coef):
        for y in range(self._dy):
            for x in range(self._dx):
                self._array[y][x] *= coef

    def anyGreaterThan(self, val):
        for y in range(self._dy):
            temp = [v for v in self._array[y] if v > val]
            if len(temp) > 0:
                return True
        return False
def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()


###
### initialize variables
###     
arrayBlk = [[ 0, 1, 1, 0 ], [ 0, 1, 1, 0 ] ]

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 17
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ]
##0
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
currBlk = Matrix(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move down
        top += 1
    elif key == 'w': # rotate the block clockwise
        print('Not implemented')
        continue
    elif key == ' ': # drop the block
        print('Not implemented')
        continue
    else:
        print('Wrong key!!!')
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            print('Not implemented')
        elif key == ' ': # undo: move up
            print('Not implemented')

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        currBlk = Matrix(arrayBlk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###
