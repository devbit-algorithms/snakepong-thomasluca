class Movement:
    def __init__(self, arena, snake):
        self.__arena = arena
        self.__snake = snake
        self.placeHeadOnOrigin()
    
    def isValidMovement(self):
        if self.__arena.getPoint(self.__nextPosX, self.__nextPosY) == 1:
            return False
        return True
    
    def move(self, key):
        self.nextPosition(key)
        if(self.isValidMovement()):
            self.__snake.prepend([self.__nextPosX, self.__nextPosY])
            self.__snake.removeLast()
        else:
            self.placeHeadOnOrigin()
    
    def nextPosition(self, key):
        if key == 'z':
            self.__nextPosY = self.__snake.head()[1] - 1
        if key == 's':
            self.__nextPosY = self.__snake.head()[1] + 1
        if key == 'q':
            self.__nextPosX = self.__snake.head()[0] - 1
        if key == 'd':
            self.__nextPosX = self.__snake.head()[0] + 1
    
    def placeHeadOnOrigin(self):
        self.__nextPosX = self.__snake.head()[0]
        self.__nextPosY = self.__snake.head()[1]
