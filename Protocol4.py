import random
import time

S = 11
m = 3
n = 5
p = (random.randint(S+1, 30))
d = 0
l = []
k = []


class Protocol4():
    def __init__(self,S,m,n,p,l,d,k):
        self.S = S
        self.m = m
        self.n = n
        self.p = p
        self.l = l
        self.d = d
        self.k = k


    def shifr(self):
        print('Идет процесс шифрования...')
        i = 0
        irest = 0
        self.d = (random.randint(self.p, 99))
        self.l.append(self.d)
        while i != 4:
            self.d = (random.randint(self.p, self.l[i]))
            if self.d != self.p and self.d != self.l[i]:
                self.l.append(self.d)
                i += 1
            if self.p == self.d:
                self.l.clear()
                i = 0
                self.d = (random.randint(self.p, 99))
                self.l.append(self.d)

        i = 0
        print(self.l)

        r = ((l[0] + l[1] + l[2]) - self.S) / self.p
        Sl = self.S + r * self.p
        print(r)#print(D)
        print(Sl)
        for i in range(5):
            self.k.append(Sl % self.l[i])
        print('k = {}'.format(self.k))

    #def deshift(self):
        de = []
        i = 0
        de.append(self.l[(random.randint(0, 4))])
        while i != 2:
            self.d = self.l[(random.randint(0, 4))]

            if self.d != de[i] and self.d != de[0]:
                de.append(self.d)
                i += 1

        self.d = de[0] * de[1] * de[2]


        D = []
        #print (self.d)
        i = 0
        for i in range(m):
            D.append(((self.d / de[i]) * (self.d / de[i]) - 1) % k[i])


        Sl = Sl % self.p
        print(Sl)

        print(D)


        i = 0









start = Protocol4(S,m,n,p,l,d,k)
start.shifr()
#start.deshift()
