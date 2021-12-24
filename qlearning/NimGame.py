from HeapClass import Heap
import random

class Nim(object):
    heaps = []
    empty = []
    allHeaps = []
    numberOfHeaps = 3
    take = 0
    playerTurnNow = False

    def __init__(self, f):
        self.reset()
        self.playerTurnNow = f
        for i in range(self.numberOfHeaps):
            random_number = int(random.uniform(1,self.numberOfHeaps+2))
            self.heaps.append(Heap(i,random_number))
            self.allHeaps.append(Heap(i,random_number))
            
    def playerTurnSmart(self):
        heap = -1
        if len(self.empty) != self.numberOfHeaps:
            taken = False
            smart_or_dumb = ""
            nim_sum = 0            
            for i in range(len(self.heaps)):
                nim_sum = nim_sum^self.heaps[i].getItems()
            i = 0
            while not taken and i < len(self.heaps):
                    if nim_sum != 0:
                        t = self.heaps[i].getItems() ^ nim_sum                        
                        if t < self.heaps[i].getItems():
                            self.take = self.heaps[i].getItems() - t
                            self.heaps[i].setItems(t)
                            number = self.heaps[i].getNumber()
                            self.allHeaps[number].setItems(t)
                            heap = number
                            taken = True
                            smart_or_dumb = "smart"
                        i += 1
                    else:
                        heapNumber = int(random.uniform(0, len(self.heaps)))
                        self.take = int(random.uniform(1, self.heaps[heapNumber].getItems()))
                        number = self.heaps[heapNumber].getNumber()
                        self.heaps[heapNumber].setItems(self.heaps[heapNumber].getItems() - self.take)
                        self.allHeaps[number].setItems(self.allHeaps[number].getItems() - self.take)
                        heap = number
                        taken = True
                        smart_or_dumb = "dumb"
        if heap != -1:
            print("Computer has taken " + str(self.take) + " item(s) from " + str(heap) + " heap, " + smart_or_dumb + " move")
        self.take = 0
        self.playerTurnNow = True
        self.updateHeaps()

    def playerTurnDumb(self):
        heapNumber = int(random.uniform(0, len(self.heaps)))
        self.take = int(random.uniform(1, self.heaps[heapNumber].getItems()))
        number = self.heaps[heapNumber].getNumber()
        self.heaps[heapNumber].setItems(self.heaps[heapNumber].getItems() - self.take)
        self.allHeaps[number].setItems(self.allHeaps[number].getItems() - self.take)
        heap = heapNumber
        smart_or_dumb = "dumb"
        if heap != -1:
            print("Computer has taken " + str(self.take) + " item(s) from " + str(heap) + " heap, " + smart_or_dumb + " move")
        self.take = 0
        self.playerTurnNow = True
        self.updateHeaps()

    def checkhWin(self):
        if self.playerTurnNow: 
            return False
        else:
            return True

    def takeItems(self, n, i):
        agent = ""
        if self.playerTurnNow == True:
            agent = "Agent 1 "
        else:
            agent = "Agent 2 "
        if not self.isAllowed(n,i):
            self.playerTurnDumb()
        else:
            self.allHeaps[n].setItems(self.allHeaps[n].getItems()-i)
            self.heaps[self.getHeap(n)].setItems(self.heaps[self.getHeap(n)].getItems()-i)
            if self.nimSum() == 0:
                smart_or_dumb = "smart"
            else:
                smart_or_dumb = "dumb"
            print(agent + "has taken " + str(i) + " item(s) from " + str(n) + " heap, " + smart_or_dumb + " move")
            self.updateHeaps()
            if self.playerTurnNow == True:
                self.playerTurnNow = False
            else:
                self.playerTurnNow = True


    def updateHeaps(self):
        newHeap = []
        for i in range(len(self.heaps)):
            if self.heaps[i].getItems() != 0:
                newHeap.append(self.heaps[i])
            else:
                self.empty.append(self.heaps[i])
        self.heaps.clear()
        self.heaps = newHeap

    def nimSum(self):
        nim_sum = 0
        for i in range(len(self.heaps)):
            nim_sum = nim_sum^self.heaps[i].getItems()
        return nim_sum

    def getState(self):
        state = ""
        for i in range(self.numberOfHeaps):
            state += str(self.allHeaps[i].getItems())
            if (i!=self.numberOfHeaps-1):
                state+=" "
        return state

    def isAllowed(self,n,i):
        if self.allHeaps[n].getItems() >= i:
            return True
        else:
            return False
    
    def printHeaps(self):
        for heap in self.heaps:
            print(str(heap.getNumber()) + " heap: " + str(heap.getItems()) + " item(s) left")
        for heap in self.empty:
            print(str(heap.getNumber()) +" heap is empty")

    def getHeap(self, n):
        for i in range(self.numberOfHeaps):
            if self.heaps[i].getNumber() == n:
               return i
        return None


    def allEmpty(self):
        if len(self.empty) == self.numberOfHeaps:
            return True
        else:
            return False

    def reset(self):
        self.allHeaps.clear()
        self.heaps.clear()
        self.empty.clear()
        self.take = 0
    pass