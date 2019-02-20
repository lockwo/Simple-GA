import random
import math

class Mind(object):
    def __init__(self, num, p=[]):
        if len(p) == 0:
            self.d = []
            for i in range(num):
                randomAngle = random.uniform(-6, 6)
                if randomAngle > 6 or randomAngle < -6:
                    print('\nuh oh')
                self.d.append(randomAngle)
            self.d = self.d.copy()
        else:
            self.d = p.copy()
        self.step = 0

    def mutation(self):
        mut_rate = 0.03
        for i in range(len(self.d)):
            rand = random.random()
            if rand < mut_rate:
                self.d[i] = random.uniform(-6, 6)
        