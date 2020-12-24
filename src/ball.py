class Ball:
    def __init__(self, arena):
        self.__posX = 5
        self.__posY = 7
        self.__dX = 1
        self.__dY = 0
        self.__arena = arena
    
    def placeOnArena(self):
        self.__arena.setPoint(self.__posX, self.__posY)
        print(str(self.__posX) + ", " + str(self.__posY))

    # Getters / Setters
    def getX(self):
        return self.__posX
    def getY(self):
        return self.__posY
    def getDirX(self):
        return self.__dX
    def getDirY(self):
        return self.__dY

    def setPos(self, x, y):
        self.__posX = x
        self.__posY = y
        
    def setDir(self, dx, dy):
        self.__dX = dx
        self.__dY = dy
    
    


