from character_frequency import character_frequency

def test_character_frequency():
    assert character_frequency("hello", "world", "test", "case", "example") == {"h": 1, "e": 5, "l": 4, "o": 2, "w": 1, "r": 1, "d": 1, "t": 3, "s": 2, "c": 2, "a": 2, "x": 1, "m": 1, "p": 1}