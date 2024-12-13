from jar import Jar
import pytest

def test_init():
    jar = Jar(6)
    assert jar.capacity == 6
    with pytest.raises(ValueError):
        Jar(-3)
    with pytest.raises(ValueError):
        Jar(3.5)

def test_deposit():
    jar= Jar(5)
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.deposit(3)

def test_withdraw():
    jar = Jar(5)
    jar._size = 3
    jar.withdraw(2)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.withdraw(2)

def test_size():
    jar = Jar()
    jar._capacity = 5
    jar._size = 4
    assert jar.size == 4
    jar.size = 3
    with pytest.raises(ValueError):
        jar.size = 6
    with pytest.raises(ValueError):
        jar.size =  -3
    with pytest.raises(ValueError):
        jar.size = 3.5

