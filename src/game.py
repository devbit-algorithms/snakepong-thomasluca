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
        self.snake = Snake(self.__arena)
        self.__movement = Movement(self.__arena, self.snake)
        self.cls()
        self.gameloop()

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def gameloop(self):
        self.__wall.placeWalls()
        self.snake.placeOnArena()
        self.__arena.printArena()
        __counter = 0
        self.__key = 'z'
        while True:
            __counter += 1
            self.__arena.clear()
            if __counter > 3:
                __counter = 0
                self.cls()
                if msvcrt.kbhit():
                    self.__key = msvcrt.getwch()
                self.update()
            time.sleep(.05)
        
    def update(self):
        self.__movement.move(self.__key)
        self.snake.placeOnArena()
        self.__movement.moveBall()
        self.__arena.printArena()

