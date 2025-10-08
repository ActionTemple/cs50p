

from hello import hello

def test_default():
    assert hello() == "Hello, world"

def test_string():
    assert hello("Andrew") == "Hello, Andrew"

