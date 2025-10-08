
# Test Working 9 to 5
# Andrew Waddington



import pytest
from working import convert




def test_hours():
    assert convert("9 to 5") != "08:00 to 05:00"
    assert convert("9 to 5") != "10:00 to 05:00"
    assert convert("9 AM to 5 AM") != "08:00 to 05:00"
    assert convert("9 AM to 5 AM") != "10:00 to 05:00"
    assert convert("1 PM to 5 AM") != "14:00 to 05:00"
    assert convert("1 PM to 5 AM") != "12:00 to 05:00"
    assert convert("08:00 to 5:00") != "09:00 to 05:00"
    assert convert("08:00 to 5:00") != "07:00 to 05:00"
    assert convert("11:00 AM to 05:00 PM") != "11:00 to 18:00"
    assert convert("11:00 AM to 05:00 PM") != "11:00 to 16:00"



def test_minutes():
    assert convert("9:30 to 5:00") != "09:35 to 05:00"
    assert convert("9:30 to 5:00") != "09:25 to 05:00"
    assert convert("9:30 to 5:00") != "09:30 to 05:05"
    assert convert("9:30 to 5:00") != "09:30 to 04:55"
    assert convert("2:45 AM to 8 PM") != "02:50 to 20:00"
    assert convert("2:45 AM to 8 PM") != "02:40 to 20:00"
    assert convert("2:45 AM to 8 PM") != "02:45 to 20:05"
    assert convert("2:45 AM to 8 PM") != "02:45 to 19:55"
    assert convert("9 to 5") != "08:00 to 05:00"


def test_valueerror():
    with pytest.raises (ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises (ValueError):
        convert("9 am to 5 pm")
    with pytest.raises (ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises (ValueError):
        convert("09:00 AM 17:00 PM")
    with pytest.raises (ValueError):
        convert("cat")
    with pytest.raises (ValueError):
        convert("9 5")
    with pytest.raises (ValueError):
        convert("09:00 - 17:00")
    with pytest.raises (ValueError):
        convert("09:00-17:00")
    with pytest.raises (ValueError):
        convert("00 AM to 00 PM")
    with pytest.raises (ValueError):
        convert("10:7 AM - 5:1 PM")
    with pytest.raises (ValueError):
        convert("09:00 to 17:00")
    with pytest.raises (ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises (ValueError):
        convert("9 am to 5 pm")
    with pytest.raises (ValueError):
        convert("9:07 AM 5:00 PM")

def test_general():
    assert convert("9 to 5") == "09:00 to 05:00"
    assert convert("11 AM to 9 PM") == "11:00 to 21:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("1 AM to 12 PM") == "01:00 to 12:00"
    assert convert("2 AM to 12 PM") == "02:00 to 12:00"
    assert convert("3 AM to 12 PM") == "03:00 to 12:00"
    assert convert("4 AM to 12 PM") == "04:00 to 12:00"
    assert convert("5 AM to 12 PM") == "05:00 to 12:00"
    assert convert("6 AM to 12 PM") == "06:00 to 12:00"
    assert convert("7 AM to 12 PM") == "07:00 to 12:00"
    assert convert("8 AM to 12 PM") == "08:00 to 12:00"
    assert convert("9 AM to 12 PM") == "09:00 to 12:00"
    assert convert("10 AM to 12 PM") == "10:00 to 12:00"
    assert convert("11 AM to 12 PM") == "11:00 to 12:00"
    assert convert("0 AM to 12 PM") == "00:00 to 12:00"
    assert convert("1 PM to 12 PM") == "13:00 to 12:00"
    assert convert("2 PM to 12 PM") == "14:00 to 12:00"
    assert convert("3 PM to 12 PM") == "15:00 to 12:00"
    assert convert("4 PM to 12 PM") == "16:00 to 12:00"
    assert convert("5 PM to 12 PM") == "17:00 to 12:00"
    assert convert("6 PM to 12 PM") == "18:00 to 12:00"
    assert convert("7 PM to 12 PM") == "19:00 to 12:00"
    assert convert("8 PM to 12 PM") == "20:00 to 12:00"
    assert convert("9 PM to 12 PM") == "21:00 to 12:00"
    assert convert("10 PM to 12 PM") == "22:00 to 12:00"
    assert convert("11 PM to 12 PM") == "23:00 to 12:00"
    assert convert("12 PM to 1 AM") == "12:00 to 01:00"
    assert convert("12 PM to 2 AM") == "12:00 to 02:00"
    assert convert("12 PM to 3 AM") == "12:00 to 03:00"
    assert convert("12 PM to 4 AM") == "12:00 to 04:00"
    assert convert("12 PM to 5 AM") == "12:00 to 05:00"
    assert convert("12 PM to 6 AM") == "12:00 to 06:00"
    assert convert("12 PM to 7 AM") == "12:00 to 07:00"
    assert convert("12 PM to 8 AM") == "12:00 to 08:00"
    assert convert("12 PM to 9 AM") == "12:00 to 09:00"
    assert convert("12 PM to 10 AM") == "12:00 to 10:00"
    assert convert("12 PM to 11 AM") == "12:00 to 11:00"
    assert convert("12 PM to 12 PM") == "12:00 to 12:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"

def test_hours_off_by_one():
    assert convert("1 PM to 5 AM") == "13:00 to 05:00"
    assert convert("2 PM to 3 PM") == "14:00 to 15:00"

def test_further():

    assert convert("06:00 to 11:00") == "06:00 to 11:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("9:07 AM to 5:00 PM") =="09:07 to 17:00"
   # assert convert("0 AM to 0 PM") == "00:00 to 12:00"


