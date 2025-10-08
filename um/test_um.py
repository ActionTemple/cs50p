


import pytest

from um import count

def test_count():
    assert count("My cat is um drinking um again um on um a park bench") == 4
    assert count("yummy mummy") == 0
    assert count("Kum by um, Yah, my um, Lord") == 2
    assert count("Um po po") == 1
    assert count(" um um um um ") == 4

