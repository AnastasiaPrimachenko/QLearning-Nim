from QAgent import QLearning
from NimGame import Nim
import random
import numpy

number_of_games = 50000
nim = Nim(True)
q = QLearning(nim)
for i in range(1, number_of_games+1):
    adv = True
    reward = 0
    start = 0
    firstTurn = int(random.uniform(0,2))
    if firstTurn == 1:
        nim = Nim(True)
        print("Player has first move")
    else:
        nim = Nim(False)
        print("Computer has first move")
    if nim.nimSum() != 0:
        adv = True
        print("Advantageous position")
    else:
        adv = False
        print("Disadvantageous position")

    while not nim.allEmpty():
        if reward != q.illegalReward:
            nim.printHeaps()
        if firstTurn:
            reward = 0
            q.stateIndex = q.states.index(nim.getState()) #индекс текущего состояние
            actionTaken = q.make_move(nim)
            if actionTaken != None:
                nim.takeItems(int(actionTaken[0]),int(actionTaken[1]))
            else:
                reward = q.illegalReward
            if not nim.allEmpty() and reward != q.illegalReward:
                nim.playerTurnDumb()
            nextState = q.states.index(nim.getState())
            q.set_nextState(nextState)
            q.update_table()

        else:
            if reward != q.illegalReward:
                nim.playerTurnDumb()                
            if start != 0 and not nim.allEmpty():
                nextState = q.states.index(nim.getState())
                q.set_nextState(nextState)
                q.update_table()
            if not nim.allEmpty():
                q.stateIndex = q.states.index(nim.getState())
                reward = 0
                actionTaken = q.make_move(nim)
                if actionTaken != None:
                    start+=1
                    nim.takeItems(int(actionTaken[0]),int(actionTaken[1]))
                else:
                    reward = q.illegalReward
    if (nim.checkhWin()):
        reward = q.winReward
        print("==============================Agent won " + str(i) + " =========================")
    else: 
        reward = q.loseReward
        print("==============================Agent lost " + str(i) + " =========================")
    nextState = q.states.index(nim.getState())
    q.reward = reward
    q.set_nextState(nextState)
    q.update_table()




winningPosition = 0 
win = 0
for i in range(1000):
    stateIndex = 0
    firstTurn = int(random.uniform(0,2))
    if firstTurn == 1:
        nim = Nim(True)
        print("Player has first move")
    else:
        nim = Nim(False)
        print("Computer has first move")
    if nim.nimSum() != 0:
        adv = True
        print("Advantageous position")
    else:
        adv = False
        print("Disadvantageous position")
    if firstTurn == 0 and nim.nimSum() == 0:
        winningPosition += 1
    elif firstTurn == 1 and nim.nimSum() != 0:
        winningPosition += 1
    while not nim.allEmpty():
        nim.printHeaps()
        if firstTurn:  
            stateIndex = q.states.index(nim.getState()) #индекс текущего состояние            
            actionIndex = numpy.argmax(q.q_table[stateIndex]) #выбираем ход с наибольшим значением   
            actionTaken = q.actions[actionIndex].split()         
            nim.takeItems(int(actionTaken[0]),int(actionTaken[1])) #можно ли так ходить
            if (not nim.allEmpty()):
                nim.playerTurnSmart()  
            #stateIndex = q.states.index(nim.getState()) #индекс текущего состояние
        else:
            nim.playerTurnSmart()             
            if (not nim.allEmpty()):
                stateIndex = q.states.index(nim.getState())          
                actionIndex = numpy.argmax(q.q_table[stateIndex]) #выбираем ход с наибольшим значением   
                actionTaken = q.actions[actionIndex].split()         
                nim.takeItems(int(actionTaken[0]),int(actionTaken[1])) #можно ли так ходить   
    if (nim.checkhWin()):
        win += 1
        print("==============================Agent won" + str(i) + " =========================")
    else:
        print("==============================Agent lost" + str(i) + " =========================")
print("Winning positions: "+str(winningPosition)+" , won: "+str(win))