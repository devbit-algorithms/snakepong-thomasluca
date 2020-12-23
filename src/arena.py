import numpy as np

class Arena:
    def __init__(self):
        self.__WIDTH = 30
        self.__HEIGHT = 15
        self.__arena = np.full((self.__HEIGHT, self.__WIDTH), 0)
    
    def printArena(self):
        for y in range(self.__HEIGHT):
            for x in range(self.__WIDTH):
                if self.__arena[y][x].any() == 1:
                    print("██", end='')
                else:
                    print(". ", end='')
            print(end="\n")

    # Getters and Setters
    def setPoint(self, x, y):
        self.__arena[y][x] = 1

    def clearPoint(self, x, y):
        self.__arena[y][x] = 0

    def getPoint(self, x, y):
        return self.__arena[y][x]

    
    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT