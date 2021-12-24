class Heap(object):

    def __init__(self, n, i):
        self.number = int(n)
        self.items = int(i)

    def getNumber(self):
        return self.number

    def getItems(self):
        return self.items

    def setNumber(self, n):
        self.number = int(n)

    def setItems(self, i):
        self.items = int(i)

    pass