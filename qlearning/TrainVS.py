from QAgent import QLearning
from NimGame import Nim
import random
import numpy

number_of_games = 10000
nim = Nim(True)
q = QLearning(nim)
q1 = QLearning(nim)
for i in range(1, number_of_games+1):
    adv = True
    rewardAgent1 = 0
    rewardAgent2 = 0
    nextStateAgent1 = 0
    nextStateAgent2 = 0
    start1 = 0
    start2 = 0
    firstTurn = int(random.uniform(0,2))
    if firstTurn == 1:
        nim = Nim(True)
        print("Agent 1 has first move")
    else:
        nim = Nim(False)
        print("Agent 2 has first move")
    if nim.nimSum() != 0:
        adv = True
        print("Advantageous position")
    else:
        adv = False
        print("Disadvantageous position")

    while not nim.allEmpty():
        if rewardAgent1 != q.illegalReward and rewardAgent2 != q.illegalReward:
            nim.printHeaps()
        if firstTurn:
            if rewardAgent2 != q.illegalReward:
                q.stateIndex = q.states.index(nim.getState())
                rewardAgent1 = 0
                actionTaken = q.make_move(nim)
                if actionTaken != None:
                    start1+=1
                    nim.takeItems(int(actionTaken[0]),int(actionTaken[1]))
                else:
                    rewardAgent1 = q.illegalReward
            if start2 != 0 and rewardAgent2 != q.illegalReward and not nim.allEmpty():
                q1.nextState = q1.states.index(nim.getState())
                q1.update_table()
            if rewardAgent1 != q.illegalReward and not nim.allEmpty():
                q1.stateIndex = q1.states.index(nim.getState())
                rewardAgent2 = 0
                actionTaken = q1.make_move(nim)
                if actionTaken != None:
                    start2+=1
                    nim.takeItems(int(actionTaken[0]),int(actionTaken[1]))
                else:
                    rewardAgent2 = q.illegalReward            
            if start1 != 0 and rewardAgent1 != q.illegalReward and not nim.allEmpty():
                q.nextState = q.states.index(nim.getState())
                q.update_table()
        else:
            if rewardAgent1 != q.illegalReward:
                q1.stateIndex = q1.states.index(nim.getState())
                rewardAgent2 = 0
                actionTaken = q1.make_move(nim)
                if actionTaken != None:
                    start2+=1
                    nim.takeItems(int(actionTaken[0]),int(actionTaken[1]))
                else:
                    rewardAgent2 = q.illegalReward            
            if start1 != 0 and rewardAgent2 != q.illegalReward and not nim.allEmpty():
                q.nextState = q.states.index(nim.getState())
                q.update_table()
            if not nim.allEmpty() and rewardAgent2 != q.illegalReward:
                q.stateIndex = q.states.index(nim.getState())
                rewardAgent1 = 0
                actionTaken = q.make_move(nim)
                if actionTaken != None:
                    start1+=1
                    nim.takeItems(int(actionTaken[0]),int(actionTaken[1]))
                else:
                    rewardAgent1 = q.illegalReward
            if start2 != 0 and rewardAgent1 != q.illegalReward and not nim.allEmpty():
                q1.nextState = q1.states.index(nim.getState())
                q1.update_table()
    if (nim.checkhWin()):
        rewardAgent1 = q.winReward
        rewardAgent2 = q.loseReward
        print("==============================Agent 1 won " + str(i) + " =========================")

    else: 
        rewardAgent1 = q.loseReward
        rewardAgent2 = q.winReward
        print("==============================Agent 1 lost " + str(i) + " =========================")
    nextState = q.states.index(nim.getState())
    q.reward = rewardAgent1
    q1.reward = rewardAgent2
    q.nextState = q.states.index(nim.getState())
    q1.nextState = q1.states.index(nim.getState())
    q.update_table()
    q1.update_table()

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
            stateIndex = q.states.index(nim.getState())           
            actionIndex = numpy.argmax(q.q_table[stateIndex])  
            actionTaken = q.actions[actionIndex].split()         
            nim.takeItems(int(actionTaken[0]),int(actionTaken[1])) 
            if (not nim.allEmpty()):
                nim.playerTurnSmart()  
        else:
            nim.playerTurnSmart()             
            if (not nim.allEmpty()):
                stateIndex = q.states.index(nim.getState())          
                actionIndex = numpy.argmax(q.q_table[stateIndex])
                actionTaken = q.actions[actionIndex].split()         
                nim.takeItems(int(actionTaken[0]),int(actionTaken[1]))   
    if (nim.checkhWin()):
        win += 1
        print("==============================Agent won " + str(i) + " =========================")
    else:
        print("==============================Agent lost " + str(i) + " =========================")
print("Winning positions: "+str(winningPosition)+" , won: "+str(win))