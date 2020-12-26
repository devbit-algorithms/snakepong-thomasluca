import random
from ball import Ball
from paddle import Paddle

class Movement:
    def __init__(self, arena, snake):
        self.__isGameOver = False
        self.__arena = arena
        self.__snake = snake
        self.placeHeadOnOrigin()
        self.__ball = Ball(self.__arena)
        self.__ball.placeOnArena()
        self.__paddle = Paddle(self.__arena)
        self.__paddle.placeOnArena()
        self.__previousKey = 'z'
        
        
    def isValidMovement(self, x, y):
        if self.__arena.getPoint(x, y) >= 1:
            return False
        return True
    
    def moveSnake(self, key):
        self.nextPosition(key)
        if(self.isValidMovement(self.__nextPosX, self.__nextPosY)):
            self.__snake.prepend([self.__nextPosX, self.__nextPosY])
            self.__snake.placeOnArena()
            if self.__ball.isGoal():
                self.__ball.reset()
            else:
                self.__snake.removeLast()
        else:
            self.__isGameOver = True

    
    def nextPosition(self, key):
        if key == 'z':
            self.__nextPosY = self.__snake.head()[1] - 1
        if key == 's':
            self.__nextPosY = self.__snake.head()[1] + 1
        if key == 'q':
            self.__nextPosX = self.__snake.head()[0] - 1
        if key == 'd':
            self.__nextPosX = self.__snake.head()[0] + 1
    
    def isOppositeKey(self, key, nextKey):
        if key == 'z' and nextKey == 's':
            return True
        if key == 's' and nextKey == 'z':
            return True
        if key == 'q' and nextKey == 'd':
            return True
        if key == 'd' and nextKey == 'q':
            return True
        return False
    
    def placeHeadOnOrigin(self):
        self.__nextPosX = self.__snake.head()[0]
        self.__nextPosY = self.__snake.head()[1]


    # Work in progress!!!
    def ballCollision(self, x, y):
        __dX = self.__ball.getDirX()
        __dY = self.__ball.getDirY()

        # Collision above
        if self.__arena.getPoint(x, y - 1) >= 1:
            __dY = 1
        # Collision right
        elif self.__arena.getPoint(x+1, y) >= 1:
            __dX = -1
            __dY = random.randint(-1, 1)
        # Collision below
        elif self.__arena.getPoint(x, y+1) >= 1:
            __dY = -1
        # Collision left
        elif self.__arena.getPoint(x-1, y) >= 1:
            __dX = 1
            __dY = random.randint(-1, 1)
        self.__ball.setDir(__dX, __dY)

    def moveBall(self):
        self.__bNextPosX = self.__ball.getX() + self.__ball.getDirX()
        self.__bNextPosY = self.__ball.getY() + self.__ball.getDirY()
        if(self.isValidMovement(self.__bNextPosX, self.__bNextPosY)):
            self.__ball.setPos(self.__bNextPosX, self.__bNextPosY)
        else:
            self.ballCollision(self.__ball.getX(), self.__ball.getY())
        self.__ball.placeOnArena()
    
    def isGameOver(self):
        return self.__isGameOver

    def movePaddle(self):
        top = self.__paddle.getTop()
        if top == 1 or top == 10:
            self.__paddle.reverseDirection()
        if self.__paddle.getDirection() == 0:
            self.__paddle.moveUp()
        else:
            self.__paddle.moveDown()
        self.__paddle.placeOnArena()