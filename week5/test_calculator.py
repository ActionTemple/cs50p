
import pytest
from calculator import square




def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


        
"""
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print ("error sq2")
    try:
        assert square(3) == 9
    except AssertionError:
        print ("error sq3")
    try:
        assert square(-3) == 9
    except AssertionError:
        print ("error sq-3")
    try:
        assert square(-2) == 4
    except AssertionError:
        print ("error sq-2")
    try:
        assert square(0) == 0
    except AssertionError:
        print ("error sq0")

"""

"""
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
"""


