from movement import Movement
from arena import Arena
from snake import Snake

arena = Arena()
snake = Snake(arena)
arena.setPoint(5, 5, 5)
arena.setPoint(21, 5, 2)
movement = Movement(arena, snake)

def test_isValidMovement():
    assert movement.isValidMovement(4, 4)
    assert not movement.isValidMovement(5, 5)

def test_isOppositeKey():
    assert movement.isOppositeKey('z', 's')
    assert not movement.isOppositeKey('s', 'd')

def test_moveSnake():
    movement.moveSnake('z')
    assert not movement.isGameOver()
    movement.moveSnake('d')
    assert movement.isGameOver()

def test_movePaddle():
    assert arena.getPoint(1, 4) == 4
    assert arena.getPoint(1, 3) == 0
    movement.movePaddle()
    assert arena.getPoint(1, 3) == 4

def test_moveBall():
    movement.moveBall()
    assert arena.getPoint(4, 7) == 2
    assert arena.getPoint(5, 7) == 0
    movement.moveBall()
    assert arena.getPoint(5, 7) == 2