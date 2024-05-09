from src.main import division, increment


def test_increment():
    assert increment(5, 3) != 3
    assert increment(2, 6) == 8


def test_division():
    assert division(5, 3) != 3
    assert division(10, 5) == 2
