import keyboard
import msvcrt
import os
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
        self.__wall.placeWalls()
        self.cls()
        self.snake.placeOnArena()
        self.__arena.printArena()
        self.gameloop()

    def cls(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def gameloop(self):
      while True:
        if msvcrt.kbhit():
            self.__movement.move(msvcrt.getwch())
            self.cls()
            self.__arena.clear()
            self.snake.placeOnArena()
            self.__arena.printArena()

