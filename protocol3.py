import random



dict = {}
l = {}

S = 11
m = 3
n = 5
x = 1
y = 0


aOne = (random.randint(1, 99))
aTwo = (random.randint(1, 99))

p = (random.randint(40, 99))


class protocol3():
    def __init__(self,dict,l,S,m,n,x,aOne,aTwo,p,y):
        self.dict = dict
        self.l = l
        self.S = S
        self.m = m
        self.n = n
        self.x = x
        self.aOne = aOne
        self.aTwo = aTwo
        self.p = p
        self.y = y

    def shifr(self):

        for self.x in range(self.n):

            self.y = (self.aOne * (self.x ** 2) + self.aTwo * self.x + self.S) % self.p
            self.x += 1
            self.dict[self.x] = self.y

        print ("p = {}".format(self.p))
        print (self.dict)

start = protocol3(dict,l,S,m,n,x,aOne,aTwo,p,y)
start.shifr()