class _Node:
    def __init__(self, element, nextNode):
        self.__element = element
        self.__next = nextNode

    def get(self):
        return self.__element

    def next(self):
        return self.__next
    
    def setNext(self, element):
        self.__next = element

class Snake:
    def __init__(self, arena, first = None):
        self.__head = first
        self.__arena = arena
        self.snake = None
        self.createInitialSnake()

    def head(self):
        if self.isEmpty():
            return None
        else:
            return self.__head.get()
    
    def tail(self):
        if self.isEmpty():
            return Snake(self.__arena)
        else:
            return Snake(self.__head.next())

    def prepend(self, element):
        self.__head = _Node(element, self.__head)
        return self

    def isEmpty(self):
        if self.__head is None:
            return True
        else:
            return False
    
    def size(self):
        def count(n, node):
            if node is None:
                return n
            else:
                return count(n+1, node.next())

        return count(0, self.__head)

    def removeLast(self):
        if self.isEmpty() or self.__head.next() == None:
            return None
        secondLast = self.__head
        while secondLast.next().next() is not None:
            secondLast = secondLast.next()
        secondLast.setNext(None)

    def createInitialSnake(self):
        self.prepend([20, 9]).prepend([20, 8]).prepend([20, 7]).prepend([20, 6])

    def placeOnArena(self):
        __currentNode = self.__head
        for i in range(self.size()):
            self.__arena.setPoint(__currentNode.get()[0], __currentNode.get()[1], 3)
            __currentNode = __currentNode.next()

    def didHeadCollideWithBody(self):
        __bodyElement = self.__head.next().next().next()
        for i in range(self.size() - 3):
            if self.__head.get() == __bodyElement.get():
                return True
            __bodyElement = __bodyElement.next()
        return False