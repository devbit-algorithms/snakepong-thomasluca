import keyboard
import msvcrt
import os
import time
from arena import Arena
from wall import Wall
from snake import Snake
from movement import Movement

class Game:
    def __init__(self):
        self.__arena = Arena()
        self.__wall = Wall(self.__arena)
        self.__snake = Snake(self.__arena)
        self.__movement = Movement(self.__arena, self.__snake)
        self.cls()
        self.gameloop()

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def gameloop(self):
        self.__wall.placeWalls()
        self.__snake.placeOnArena()
        self.__arena.printArena()
        __counter = 0
        self.__key = 'z'
        while not self.__movement.isGameOver():
            __counter += 1
            if __counter > 10:
                self.__arena.clear()
                __counter = 0
                self.cls()
                if msvcrt.kbhit():
                    __tempKey = msvcrt.getwch()
                    if not self.__movement.isOppositeKey(self.__key, __tempKey):
                        self.__key = __tempKey
                self.update()
            time.sleep(.01)
        self.endGame()
        
        
    def update(self):
        self.__movement.movePaddle()
        self.__movement.moveSnake(self.__key)
        self.__movement.moveBall()
        self.__arena.printArena()
    
    def endGame(self):
        self.cls()
        print("\nGame Over")
        print("Your snake reached a length of " + str(self.__snake.size()) + '\n')
