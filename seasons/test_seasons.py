


# Test Seasons of Love
# Andrew Waddington


import pytest
from seasons import birthday


def test_minutes():
    with pytest.raises (ValueError):
        birthday("1980-02-30")
