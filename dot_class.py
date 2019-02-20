from mind import *
from math import * 

class Dot(object):
    def __init__(self, position, velocity, acceleration, n=None):
        if n == None:
            self.m = Mind(500)
        else:
            self.m = Mind(500, n)
        self.p = position.copy()
        self.v = velocity.copy()
        self.a = acceleration.copy()
        self.rad = 2
        self.best = False
        self.goal = False
        self.out = False
        
    
    def move(self):
        if len(self.m.d) > self.m.step:
            for i in range(2):
                self.a[i] = self.m.d[self.m.step]
                self.m.step += 1
        else: 
            self.out = True
        for i in range(2):
            self.v[i] += self.a[i]
        if self.v[0] > 5:
            self.v[0] = 5
        if self.v[0] < -5:
            self.v[0] = -5
        if self.v[1] > 5:
            self.v[1] = 5 
        if self.v[1] < -5:
            self.v[1] = -5
        for i in range(2):
            self.p[i] += self.v[i]
        
    def fitness(self):
        goal = (300, 5)
        if self.goal is True:
            fit = 40000/(self.m.step**2)
        else:
            dist = sqrt((goal[0]-self.p[0])**2+(goal[1]-self.p[1])**2)
            fit = 1/(dist**2)
        return fit
    
    def baby(self):
        return Dot([300,570], [0,0], [0,0], self.m.d.copy())
    
    def col_test(self, x0, y0, x1, y1):
        if (((x0 <= self.p[0] + self.rad <= x1) or x0 <= self.p[0] - self.rad <= x1) and ((\
            y0 <= self.p[1] + self.rad <= y1) or (y0 <= self.p[1] - self.rad <= y1))):
            self.out = True
        
                
