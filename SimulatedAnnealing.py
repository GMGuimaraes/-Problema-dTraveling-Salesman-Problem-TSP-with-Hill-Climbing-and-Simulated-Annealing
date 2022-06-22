import random
from math import exp, trunc, sqrt

class SimulatedAnnealing:

    def __init__(self, x1, x2, x3, x4,Tmax, Tmin, a, Kt):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.Tmax = Tmax
        self.Tmin = Tmin
        self.a = a
        self.Kt = Kt

    def func(self,x1,x2, x3, x4):
        return sqrt(((x1-x3)**2)+((x2-x4)**2))

    def prob(self, current, new, T):
        print(T)
        return exp(int(current - new)/T)

    def Start(self):
        current = self.func(self.x1,self.x2,self.x3,self.x4)
        while (self.Tmax > self.Tmin):
            for i in range (1,self.Kt):
                self.x1,self.x2,self.x3,self.x4 = random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1), random.uniform(-1,1)
                new = self.func(self.x1,self.x2,self.x3,self.x4)
                if (self.prob(current,new,self.Tmax) > random.random()):
                    current = new
            self.Tmax = self.Tmax * self.a
        return self.x1, self.x2, self.x3, self.x4, current
        '''
        print("Xu= ",self.x1)
        print("Yu = ",self.x2)
        print("Xv = ",self.x3)
        print("Yv = ",self.x4)
        print("resultados = ",current)
        '''