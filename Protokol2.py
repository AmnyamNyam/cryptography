import string
import random
import time
import sys

#Кодирование секрета – слово «KVA»
K = '01001011'
V = '01010110'
A = '01000001'
#Гамма 1
GammaOneA = 0
GammaOneABin = 0
GammaOneB = 0
GammaOneBBin = 0
GammaOneC = 0
GammaOneCBin = 0
#Гамма 2
GammaTwoA = 0
GammaTwoABin = 0
GammaTwoB = 0
GammaTwoBBin = 0
GammaTwoC = 0
GammaTwoCBin = 0
#Гамма 3
GammaThreeA = 0
GammaThreeABin = 0
GammaThreeB = 0
GammaThreeBBin = 0
GammaThreeC = 0
GammaThreeCBin = 0

Globalflag = 0

Alphabett = {}


class protocol2():
    def __init__(self,K,V,A,GammaOneA,GammaOneABin,GammaOneB,GammaOneBBin,GammaOneC,GammaOneCBin,GammaTwoA,GammaTwoABin,GammaTwoB,GammaTwoBBin,GammaTwoC,GammaTwoCBin,
                 GammaThreeA,GammaThreeB,GammaThreeC,GammaThreeABin,GammaThreeBBin,GammaThreeCBin,Alphabett, Globalflag):
        self.K = K
        self.V = V
        self.A = A
        self.GammaOneA = GammaOneA
        self.GammaOneB = GammaOneB
        self.GammaOneC = GammaOneC
        self.GammaOneABin = GammaOneABin
        self.GammaOneBBin = GammaOneBBin
        self.GammaOneCBin = GammaOneCBin
        self.GammaTwoA = GammaTwoA
        self.GammaTwoB = GammaTwoB
        self.GammaTwoC = GammaTwoC
        self.GammaTwoABin = GammaTwoABin
        self.GammaTwoBBin = GammaTwoBBin
        self.GammaTwoCBin = GammaTwoCBin
        self.GammaThreeA = GammaThreeA
        self.GammaThreeB = GammaThreeB
        self.GammaThreeC = GammaThreeC
        self.GammaThreeABin = GammaThreeABin
        self.GammaThreeBBin = GammaThreeBBin
        self.GammaThreeCBin = GammaThreeCBin

        self.Alphabett = Alphabett
        self.Globalflag = Globalflag

    def Alphabet(self):
        self.Alphabett = {
            "A": "01000001",
            "B": "01000010",
            "C": "01000011",
            "D": "01000100",
            "E": "01000101",
            "F": "01000110",
            "G": "01000111",
            "H": "01001000",
            "I": "01001001",
            "J": "01001010",
            "K": "01001011",
            "L": "01001100",
            "M": "01001101",
            "N": "01001110",
            "O": "01001111",
            "P": "01010000",
            "Q": "01001111",
            "R": "01010010",
            "S": "01010011",
            "T": "01010100",
            "U": "01010101",
            "V": "01010110",
            "W": "01010111",
            "X": "01011000",
            "Y": "01011001",
            "Z": "01011010"
        }

    def mathsshifr(self,secret = '',secretOneBin ='',secretTwoBin = '',secretThreeBin =''):

        self.Globalflag = 1

        self.secret = secret
        self.secretOneBin = secretOneBin
        self.secretTwoBin = secretTwoBin
        self.secretThreeBin = secretThreeBin

        #Гамма 1
        self.GammaOneA = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaOneABin = self.Alphabett[self.GammaOneA]
        self.GammaOneB = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaOneBBin = self.Alphabett[self.GammaOneB]
        self.GammaOneC = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaOneCBin = self.Alphabett[self.GammaOneC]

        #Гамма 2
        self.GammaTwoA = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaTwoABin = self.Alphabett[self.GammaTwoA]
        self.GammaTwoB = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaTwoBBin = self.Alphabett[self.GammaTwoB]
        self.GammaTwoC = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaTwoCBin = self.Alphabett[self.GammaTwoC]

        #Гамма 3

        self.GammaThreeA = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaThreeABin = self.Alphabett[self.GammaThreeA]
        self.GammaThreeB = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaThreeBBin = self.Alphabett[self.GammaThreeB]
        self.GammaThreeC = ''.join(random.choices(string.ascii_uppercase, weights=None, cum_weights=None, k=1))
        self.GammaThreeCBin = self.Alphabett[self.GammaThreeC]



        #Вычисление шифрограммы

        self.secretOneBin = int(self.K, base=2) + int(self.GammaOneABin, base=2) + int(self.GammaTwoABin, base=2) + int(self.GammaThreeABin, base=2)
        self.secretTwoBin = int(self.V, base=2) + int(self.GammaOneBBin, base=2) + int(self.GammaTwoBBin, base=2) + int(self.GammaThreeBBin, base=2)
        self.secretThreeBin = int(self.A, base=2) + int(self.GammaOneCBin, base=2) + int(self.GammaTwoCBin, base=2) + int(self.GammaThreeCBin, base=2)

        self.secretOneBin = bin(self.secretOneBin)
        self.secretTwoBin = bin(self.secretTwoBin)
        self.secretThreeBin = bin(self.secretThreeBin)

        self.secret = str(self.secretOneBin) + ' ' + str(self.secretTwoBin)+ ' ' + str(self.secretThreeBin)

        print('Шифрограмма: {}'.format(self.secret))
        start.startscreen()

        #Восстановление секрета


    def mathdeshifr(self, desecret = ''):

        if self.Globalflag == 0:
            print("ОШИБКА! Нет шифрующего элемента.")
            start.startscreen()

        self.desecret = desecret

        self.K = int(self.secretOneBin, base=2) - int(self.GammaOneABin, base=2) - int(self.GammaTwoABin, base=2) - int(self.GammaThreeABin, base=2)
        self.V = int(self.secretTwoBin, base=2) - int(self.GammaOneBBin, base=2) - int(self.GammaTwoBBin, base=2) - int(self.GammaThreeBBin, base=2)
        self.A = int(self.secretThreeBin, base=2) - int(self.GammaOneCBin, base=2) - int(self.GammaTwoCBin, base=2) - int(self.GammaThreeCBin, base=2)

        self.K = bin(self.K)
        self.V = bin(self.V)
        self.A = bin(self.A)

        self.desecret = str(self.K) + ' ' + str(self.V) + ' ' + str(self.A)

        print('Секрет: {}'.format(self.desecret))
        start.startscreen()

    def startscreen(self, inputWord=0):
        print("Разбиение секрета с помощью гаммирования by Amnyam v0.8\n")
        self.inputWord = inputWord
        self.inputWord = input()

        # ПЕТРОВИЧ, ЗАВОДИ КОЛХОЗ!

        if self.inputWord == 'start -sh':
            start.Alphabet()
            start.mathsshifr()
        elif self.inputWord == 'start -de':
            start.mathdeshifr()
        elif self.inputWord == 'debug':
            start.debug()
        elif self.inputWord == 'refresh':
            start.randomRestart()
        elif self.inputWord == 'exit':
            start.exit()
        elif self.inputWord == 'help':
            start.help()
        else:
            print('ОШИБКА! Такой команды не существует. Используй help для получения списка команд')
            start.startscreen()

    def randomRestart(self):
        print('WiP')
        start.startscreen()



    def help(self):
        print("start\n")
        print("-sh - запуск шифратора\n")
        print("-de - запуск дешифратора\n")
        print("\n")
        print("debug - отобразить все переменные\n")
        print("refresh - генерация случайных гамм\n")
        print("exit - закрыть программу")
        start.startscreen()

    def debug(self):

        print('Гамма 1\n')
        print('{} = {} | {} = {} | {} = {}'.format(self.GammaOneA,self.GammaOneABin,self.GammaOneB,self.GammaOneBBin,
                                                   self.GammaOneC,self.GammaOneCBin))
        print('Гамма 2\n')
        print('{} = {} | {} = {} | {} = {}'.format(self.GammaTwoA, self.GammaTwoABin, self.GammaTwoB, self.GammaTwoBBin,
                                                   self.GammaTwoC, self.GammaTwoCBin))
        print('Гамма 3\n')
        print('{} = {} | {} = {} | {} = {}'.format(self.GammaThreeA, self.GammaThreeABin, self.GammaThreeB, self.GammaThreeBBin,
                                                   self.GammaThreeC, self.GammaThreeCBin))



        start.startscreen()

    def exit(self):
        print('Выход завершен')
        sys.exit()




start = protocol2(K,V,A,GammaOneA,GammaOneABin,GammaOneB,GammaOneBBin,GammaOneC,GammaOneCBin,GammaTwoA,GammaTwoABin,GammaTwoB,GammaTwoBBin,GammaTwoC,GammaTwoCBin,
                 GammaThreeA,GammaThreeB,GammaThreeC,GammaThreeABin,GammaThreeBBin,GammaThreeCBin,Alphabett,Globalflag)

start.startscreen()




