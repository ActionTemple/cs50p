

# Test Working 9 to 5
# Andrew Waddington



import pytest
from working import convert

#def test_hours():
 #   assert convert("9:00 to 5:00") != "08:00 to 05:00"


def test_valueerror():
    with pytest.raises (ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises (ValueError):
        convert("9:00 AM 5:00 PM")

def test_hours_off_by_one():
    assert convert("1 PM to 5 AM") != "14:00 to 05:00"  
    assert convert("11 AM to 9 PM") != "12:00 to 21:00"
    assert convert("12 PM to 1 AM") != "11:00 to 01:00"
    assert convert("12 AM to 12 PM") != "01:00 to 12:00"

    assert convert("9 AM to 5 AM") == "09:00 to 05:00"

