import numpy
import time
import os
import random
import copy
class LifeGame(object):
    def __init__(self,shape=(15,15)):
        '''size is a tuple(a,b),a is width,b is length'''
        self._map = numpy.array([[1 if random.randint(0,100) >80 else 0 for i in range(shape[0])] for j in range(shape[1])])
        self._map.shape = shape
        self.shape = shape
        self.draw_map = [[' ' for i in range(shape[0])] for j in range(shape[1])]
        self._next_map = numpy.zeros(shape)
        self.nextxy = [[0,1],[1,0],[-1,0],[0,-1],[-1,1],[1,-1],[1,1],[-1,-1]]
    def next_map(self):
        '''calc the next map'''
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                cnt1 = 0
                for k in range(8):
                    x = i+self.nextxy[k][0]
                    y = j+self.nextxy[k][1]
                    if x >= 0 and x < self.shape[0] and y >= 0 and y < self.shape[1]:
                        if self._map[x][y] == 1:
                            cnt1 += 1
                if cnt1 == 3:
                    self._next_map[i][j] = 1
                elif cnt1 == 2:
                    self._next_map[i][j] = self._map[i][j]
                else:
                    self._next_map[i][j] = 0  
                if self._next_map[i][j] == 0:
                    self.draw_map[i][j] = '.'
                else: self.draw_map[i][j] = '▇'
        self._map = copy.deepcopy(self._next_map)
        return self.draw_map 
                
    def draw(self,mp,x=15,y=15):
        tmp = numpy.array(mp)
        for i in range(x):
            for j in range(y):
                print(mp[i][j],end='  ')
            print('\n')
    def start(self,sleeptime=1):
        os.system('clear')
        self.draw(self.next_map())
        time.sleep(sleeptime)  

if __name__ == '__main__':
    lifegame = LifeGame()
    while True:
        lifegame.start()

