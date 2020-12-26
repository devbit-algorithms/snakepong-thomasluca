import numpy as np

class Arena:
    def __init__(self):
        self.__WIDTH = 30
        self.__HEIGHT = 15
        self.__arena = np.full((self.__HEIGHT, self.__WIDTH), 0)
    
    def printArena(self):
        output = ""
        for y in range(self.__HEIGHT):
            for x in range(self.__WIDTH):
                if self.__arena[y][x] == 2:
                    output += "\033[;31m██\033[0m"
                elif self.__arena[y][x] == 3:
                    output += "\033[;32m██\033[0m"
                elif self.__arena[y][x] == 4:
                    output += ".|"
                elif self.__arena[y][x] == 1:
                    output += "██"
                else:
                    output += ". "
            output += "\n"
        print(output)
    
    def clear(self):
        for y in range(1, self.__HEIGHT - 1):
            for x in range(1, self.__WIDTH - 1):
                self.__arena[y][x] = 0

    # Getters and Setters
    def setPoint(self, x, y, material):
        self.__arena[y][x] = material

    def clearPoint(self, x, y):
        self.__arena[y][x] = 0

    def getPoint(self, x, y):
        return self.__arena[y][x]

    
    def getWidth(self):
        return self.__WIDTH

    def getHeight(self):
        return self.__HEIGHT