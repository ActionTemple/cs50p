

# Test_Jar
# Andrew Waddington

import pytest
from jar import Jar


def test_init():
    jar = Jar()
    with pytest.raises (ValueError):
        jar.withdraw(13)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(1) != 1


def test_withdraw():
    jar = Jar()
    assert jar.withdraw(-1) != 1
