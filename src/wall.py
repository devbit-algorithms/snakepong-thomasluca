class Wall:
    def __init__(self, arena):
        self.__arena = arena

    def placeWalls(self):
        for height in range(self.__arena.getHeight()):
            for width in range(self.__arena.getWidth()):
                if (height==0 or height==self.__arena.getHeight() - 1 or width==0 or width==self.__arena.getWidth() - 1):
                    self.__arena.setPoint(width, height, 1)
