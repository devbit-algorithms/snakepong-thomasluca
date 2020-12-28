from arena import Arena

def test_getWidth():
    arena = Arena()
    assert arena.getWidth() == 30

def test_getHeight():
    arena = Arena()
    assert arena.getHeight() == 15

def test_setPoint_getPoint():
    arena = Arena()
    assert arena.getPoint(5, 5) == 0
    arena.setPoint(5, 5, 5)
    assert arena.getPoint(5, 5) == 5
    assert arena.getPoint(5, 5) != 0

def test_clearPoint():
    arena = Arena()
    arena.setPoint(1, 1, 1)
    assert arena.getPoint(1, 1) == 1
    arena.clearPoint(1, 1)
    assert arena.getPoint(1, 1) == 0

def test_clear():
    arena = Arena()
    arena.setPoint(1, 1, 2)
    arena.setPoint(1, 2, 3)
    assert arena.getPoint(1, 2) == 3
    arena.clear()
    assert arena.getPoint(1, 2) == 0
    assert arena.getPoint(1, 1) == 0