
# test_numb3rs
# Andrew Waddington

import pytest
from numb3rs import validate


def test_validate():
    assert validate("192.168.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.1000") == False
    assert validate("500.255.255.255") == False
    assert validate("255.888.255.255") == False
    assert validate("255.255.888.255") == False
    assert validate("255.255.255.888") == False

def test_first_byte():
    assert validate("300.10.233.45") == False
    assert validate("1000.10.233.45") == False

def test_five_byte():
    assert validate("178.33.24.89.10") == False

def test_input_cat():
    assert validate("cat") == False
