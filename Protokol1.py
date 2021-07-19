import random
import time
import sys

# Буквы. Здесь указывается начальная сумма.
K = 0
V = 0
A = 0
# Высирает случайное число от 1 до 9.
randomNumber = (random.randint(1, 9))
# Открытые ключи. Случайные числа от 1 до 99. Ключи nK, nV, nA всегда равны. Наверное.
eK = (random.randint(1, 99))
nK = (random.randint(1, 99))
eV = (random.randint(1, 99))
nV = nK
eA = (random.randint(1, 99))
nA = nK
# Закрытые ключи. Случайные числа от 1 до 99.
dK = (random.randint(1, 99))
dV = (random.randint(1, 99))
dA = (random.randint(1, 99))
# Средняя зарплата.
ZP = 0
# Результаты вычислений, которые отсылают друг другу K,V,A. Нужно для дебагинга.
resultK = 0
resultV = 0
resultA = 0
#Флаг, который позволит не выбрасывать пользователя во время обновления чисел. Смотри функцию debug.
randFlag = 0



class protocol():
    def __init__(self,K,V,A,randomNumber, eK, nK, eV, nV, eA, nA, dK, dV, dA, ZP, resultK, resultV,resultA,randFlag):
        self.K = K
        self.V = V
        self.A = A
        self.randomNumber = randomNumber
        self.eK = eK
        self.nK = nK
        self.eV = eV
        self.nV = nV
        self.eA = eA
        self.nA = nA
        self.dK = dK
        self.dV = dV
        self.dA = dA
        self.ZP = ZP
        self.resultK = resultK
        self.resultV = resultV
        self.resultA = resultA
        self.randFlag = randFlag


    def input(self):
        try:
            self.K = int(input('Укажите число для K: '))
            self.V = int(input('Укажите число для V: '))
            self.A = int(input('Укажите число для A: '))
        except ValueError:
            print('Это не числа!\n')
            start.input()

    def startscreen(self, inputWord = 0):
        print("Протокол конфиденциального вычисления by Amnyam v1.0\n")
        print("start - запуск, debug - отобразить все переменные\n")
        print("refresh - обновить случайные числа, exit - закрыть программу")
        self.inputWord = inputWord
        self.inputWord = input()

        #ПЕТРОВИЧ, ЗАВОДИ КОЛХОЗ!

        if self.inputWord == 'start':
            start.input()
            start.maths()
            self.debugFlag = 1
        elif self.inputWord == 'debug':
            start.debug()
        elif self.inputWord == 'refresh':
            start.randomRestart()
        elif self.inputWord == 'exit':
            start.exit()
        else:
            print('ОШИБКА! Такой команды не существует.')
            start.startscreen()


    def debug(self):
        print('Буквы. Здесь указывается начальная сумма:\n')
        print('K = {} | V = {} | A = {}'.format(self.K,self.V,self.A))
        print('================================\n')
        print('Случайное число от 1 до 9:\n')
        print('randomNumber = {}'.format(self.randomNumber))
        print('================================\n')
        print('Открытые ключи. Случайные числа от 1 до 99. Ключи nK, nV, nA всегда равны. Наверное.\n')
        print('eK = {} | eV = {} | eA = {}'.format(self.eK,self.eV,self.eA))
        print('nK = {} | nV = {} | nA = {}'.format(self.nK,self.nV,self.nA))
        print('================================\n')
        print('Закрытые ключи. Случайные числа от 1 до 99.\n')
        print('dK = {} | dV = {} | dA = {}'.format(self.dK, self.dV, self.dA))
        print('================================\n')
        print('Средняя зарплата.\n')
        print('ZP = {}'.format(self.ZP))
        print('================================\n')
        print('Результаты вычислений, которые отсылают друг другу K,V,A.\n')
        print('resultK = {} | resultV = {} | resultA = {}'.format(self.resultK, self.resultV, self.resultA))
        print('================================\n')
        print('Флаг, который позволит не выбрасывать пользователя во время обновления чисел.\n')
        print('randFlag = {}'.format(self.randFlag))
        print('================================\n')

        start.startscreen()



    def randomRestart(self):
        self.randomNumber = (random.randint(1, 9))
        self.eK = (random.randint(1, 99))
        self.nK = (random.randint(1, 99))
        self.eV = (random.randint(1, 99))
        self.nV = self.nK
        self.eA = (random.randint(1, 99))
        self.nA = self.nK
        self.dK = (random.randint(1, 99))
        self.dV = (random.randint(1, 99))
        self.dA = (random.randint(1, 99))
        print('Числа обновлены!')

        if self.randFlag == 0:
            start.startscreen()

    def exit(self):
        sys.exit()

    def maths(self):
        self.randFlag = 1
        #Честно говоря, все resultK,V,A можно заменить на ZP и результат будет таким же, однако тогда мы не сможем отследить каждый шаг.

        #A прибавляет случайное секретное число randomNumber к сумме своему числу, шифрует результат с помощью открытого ключа V и отсылает его V.
        self.resultV = (self.A + self.randomNumber) ** self.eV % self.nV

        # V расшифровывает результат, добавляет к нему свое число, шифрует результат с помощью открытого ключа K и отсылает его K.
        self.resultK = (self.V + (self.resultV ** self.dV % self.nK)) ** self.eK % self.nK

        # K расшифровывает результат, добавляет к нему свое число, шифрует результат с помощью открытого ключа A и отсылает его A.
        self.resultA = (self.K + (self.resultK ** self.dK % self.nA)) ** self.eA % self.nA

        # A расшифровывает результат, отнимает randomNumber и объявляет среднее число
        self.ZP = ((self.resultA ** self.dA % self.nA) - self.randomNumber) / 3

        if self.ZP <= 0:
            print('Амням опять наколхозил и среднее число стало отрицательным. Пересчет...\n')
            time.sleep(1)
            start.randomRestart()
            start.maths()

        self.randFlag = 0

        print('Средняя зарплата.\n')
        print('ZP = {}'.format(self.ZP))
        start.startscreen()



start = protocol(K,V,A,randomNumber, eK, nK, eV, nV, eA, nA, dK, dV, dA, ZP, resultK, resultV,resultA,randFlag)
start.startscreen()










