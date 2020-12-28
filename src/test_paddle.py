from paddle import Paddle
from arena import Arena

def test_getTop():
    paddle = Paddle(Arena())
    assert paddle.getTop() == 4

def test_moveUp():
    paddle = Paddle(Arena())
    assert paddle.getTop() == 4
    paddle.moveUp()
    assert paddle.getTop() == 3

def test_moveDown():
    paddle = Paddle(Arena())
    assert paddle.getTop() == 4
    paddle.moveDown()
    assert paddle.getTop() == 5

def test_getDirection():
    paddle = Paddle(Arena())
    assert paddle.getDirection() == 0

def test_reverseDirection():
    paddle = Paddle(Arena())
    assert paddle.getDirection() == 0
    paddle.reverseDirection()
    assert paddle.getDirection() == 1