from dot_class import *
import random

class Pop(object):
    def __init__(self, num):
        self.dot_pop = []
        self.new_dots = []
        self.gen = 1
        self.fast = 500
        for i in range(num):
            self.dot_pop.append(Dot([300,570], [0,0], [0,0]))
            self.new_dots.append(None)
        self.dot_pop = self.dot_pop.copy()
    
    def selection(self):
        fit = self.fit_sum()
        m = self.best()
        self.new_dots[0] = self.dot_pop[m].baby()
        self.new_dots[0].best = True
        i = 1
        while i < len(self.dot_pop):
            parent = self.select_parent()
            self.new_dots[i] = parent.baby()
            i += 1
        self.dot_pop = self.new_dots.copy()
        self.gen += 1
    
    def fit_sum(self):
        fitsum = 0
        for i in range(len(self.dot_pop)):
            fitsum += self.dot_pop[i].fitness()
        return fitsum
    
    def select_parent(self):
        rand = random.uniform(0,self.fit_sum())
        run = 0
        for i in range(len(self.dot_pop)):
            run += self.dot_pop[i].fitness()
            if run > rand:
                return self.dot_pop[i]
    
    def mut(self):
        i = 1
        while i < len(self.dot_pop):
            self.dot_pop[i].m.mutation()
            i += 1
            
    def best(self):
        maxx = 0
        mi = 0
        for i in range(len(self.dot_pop)):
            if self.dot_pop[i].fitness() > maxx:
                maxx = self.dot_pop[i].fitness()
                mi = i
        if self.dot_pop[mi].goal is True:
            self.fast = self.dot_pop[mi].m.step
        return mi