from separate_by_index import separate_by_index

def test_separate_by_index():
    assert separate_by_index("Hello World") == ("HloWrd", "el ol")
    