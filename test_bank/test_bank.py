
# Test Bank
# Andrew Waddington

import pytest
from bank import value

def test_hello():
    assert value("hello") == 0

def test_begin_h():
    assert value("hi") == 20

def test_other_letters():
    assert value("jobBlob") == 100

def test_case_sensitivity():
    assert value("hElLo") == 0
