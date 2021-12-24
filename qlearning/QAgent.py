from NimGame import Nim
import numpy
import random
class QLearning(object):

    def __init__(self,nim):
        self.states = []
        self.actions = []
        self.q_table = []

        self.numberOfStates = 0
        self.numberOfActions = 0

        self.alpha = 0.1
        self.gamma = 1
        self.epsilon = 0.8

        self.winReward = 1
        self.loseReward = -1
        self.illegalReward = -1000

        self.actionIndex = 0
        self.stateIndex = 0
        self.nextState = 0
        self.reward = 0

        self.numberOfStates = (nim.numberOfHeaps+2) ** nim.numberOfHeaps #количество состояний
        self.numberOfActions = (nim.numberOfHeaps+1) * nim.numberOfHeaps   #количество действий

        self.q_table = numpy.zeros([self.numberOfStates, self.numberOfActions])
        for i in range(nim.numberOfHeaps): #заполняем массив возможных действий
            for j in range(1,nim.numberOfHeaps+2):
                self.actions.append(str(i)+" "+str(j)) 
        for i in range(nim.numberOfHeaps+2): #заполняем массив возможных состояний
            for j in range(nim.numberOfHeaps+2):
                for k in range(nim.numberOfHeaps+2):
                    self.states.append(str(i)+" "+str(j)+" "+str(k))

    
    def update_table(self):
        if self.reward != self.illegalReward:
            self.oldValue = self.q_table[self.stateIndex, self.actionIndex]
            self.nextMax = self.q_table[self.nextState,numpy.argmax(self.q_table[self.nextState])]
            self.newValue = self.oldValue + self.alpha * (self.reward + self.gamma * self.nextMax - self.oldValue)
            self.q_table[self.stateIndex, self.actionIndex] = self.newValue
        else:
            self.q_table[self.stateIndex, self.actionIndex] = self.illegalReward


    def make_move(self, nim):
        self.reward = 0
        if random.random() > self.epsilon: #рандомный ход или ход по таблице
            self.actionIndex = int(random.uniform(0,self.numberOfActions))
            self.actionTaken = self.actions[self.actionIndex].split() #рандомный ход
            if nim.isAllowed(int(self.actionTaken[0]),int(self.actionTaken[1])): #можно ли так ходить
                return self.actionTaken
            else:
                self.reward = self.illegalReward
                return None
        else:                
            self.actionIndex = numpy.argmax(self.q_table[self.stateIndex]) #выбираем ход с наибольшим значением   
            self.actionTaken = self.actions[self.actionIndex].split()         
            if nim.isAllowed(int(self.actionTaken[0]),int(self.actionTaken[1])): #можно ли так ходить
                return self.actionTaken
            else:
                self.reward = self.illegalReward
                return None
    pass




