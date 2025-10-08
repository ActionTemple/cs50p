

# Test Plates
# Andrew Waddington


import pytest
from plates import is_valid

def test_CS50():
    assert is_valid("CS50") == True

def test_CS05():
    assert is_valid("CS05") == False

def test_CS50P():
    assert is_valid("CS50P") == False

def test_PI314():
    assert is_valid("PI3.14") == False

def test_H():
    assert is_valid("H") == False

def test_OUTATIME():
    assert is_valid("OUTATIME") == False

def test_no_input():
    assert is_valid("") == False
"""
def test_case():
    assert is_valid("aa55") == False
    assert is_valid("AA55") == True
"""
def test_misc():
    assert is_valid("01hjh7") == False
    assert is_valid("02hjh7") == False
    assert is_valid("03hjh7") == False
    assert is_valid("04hjh7") == False
    assert is_valid("05hjh7") == False
    assert is_valid("06hjh7") == False
    assert is_valid("07hjh7") == False
    assert is_valid("08hjh7") == False
    assert is_valid("09Abnn") == False
    assert is_valid("10yuyu") == False
    assert is_valid("20ABBH") == False
    assert is_valid("30BAAA") == False
    assert is_valid("40BBBB") == False
    assert is_valid("50BBBB") == False
    assert is_valid("60JJJJ") == False
    assert is_valid("70NNNN") == False
    assert is_valid("80HHHH") == False
    assert is_valid("90HHHH") == False
    assert is_valid(".4hjh7") == False
    assert is_valid(".5hjh7") == False
    assert is_valid("['hjh7") == False
    assert is_valid("::hjh7") == False
    assert is_valid("//hjh7") == False
    assert is_valid(".=hjh7") == False
    assert is_valid(",`hjh7") == False
    assert is_valid("AA055") == False
    assert is_valid("AAA055") == False
    assert is_valid("AAAA05") == False
    assert is_valid("AAAAA0") == False
    assert is_valid("0AAAJJ") == False
    assert is_valid("12") == False




