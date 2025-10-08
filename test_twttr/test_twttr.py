




from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"

def test_caps():
    assert shorten("HELICOPTER") == "HLCPTR"

def test_punctuation():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_numbers():
    assert shorten("J30P4RD THE L30P4RD") == "J30P4RD TH L30P4RD"
