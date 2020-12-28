from arena import Arena
from snake import Snake

def test_head():
    snake = Snake(Arena())
    assert snake.head() == [20, 6]
    assert snake.head() != [20, 5]

def test_prepend():
    snake = Snake(Arena())
    snake.prepend([19, 6])
    assert snake.head() == [19, 6]
    assert snake.head() != [20, 6]

def test_size():
    snake = Snake(Arena())
    assert snake.size() == 4
    assert snake.size() != 0
    snake.prepend([0, 0]).prepend([5, 5])
    assert snake.size() == 6

def test_removeLast():
    snake = Snake(Arena())
    assert snake.size() == 4
    snake.removeLast()
    assert snake.size() == 3

def test_didHeadCollideWithBody():
    snake = Snake(Arena())
    snake.prepend([20, 10])
    assert not snake.didHeadCollideWithBody()
    snake.prepend([20, 8])
    assert snake.didHeadCollideWithBody()
