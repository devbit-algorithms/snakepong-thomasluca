class Paddle:
    def __init__(self, arena):
        self.__LENGTH = 4
        self.__top = 4
        self.__bottom = self.__LENGTH + self.__top
        self.__direction = 0 # 1 == down, 0 == up

        self.__arena = arena
    
    def placeOnArena(self):
        for i in range(self.__LENGTH):
            self.__arena.setPoint(1, self.__top + i, 4)
    
    def moveUp(self):
        self.__top -= 1
    
    def moveDown(self):
        self.__top += 1
    
    def getTop(self):
        return self.__top
    def getDirection(self):
        return self.__direction
    def reverseDirection(self):
        self.__direction = not self.__direction
