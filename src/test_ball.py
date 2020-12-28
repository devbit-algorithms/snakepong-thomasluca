from ball import Ball
from arena import Arena

def test_getX():
    ball = Ball(Arena())
    assert ball.getX() == 3

def test_getY():
    ball = Ball(Arena())
    assert ball.getY() == 7

def test_setPos():
    ball = Ball(Arena())
    assert ball.getY() == 7
    ball.setPos(5, 6)
    assert ball.getX() == 5
    assert ball.getY() == 6

def test_setDir():
    ball = Ball(Arena())
    assert ball.getDirX() == 1
    assert ball.getDirY() == 0
    ball.setDir(-1, 1)
    assert ball.getDirX() == -1
    assert ball.getDirY() == 1

def test_isGoal():
    ball = Ball(Arena())
    assert not ball.isGoal()
    ball.setPos(1, 5)
    assert ball.isGoal()