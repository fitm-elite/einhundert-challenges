from is_word_in_list import is_word_in_list

def test_is_word_in_list_passed():
    assert is_word_in_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"], "cherry") == True

def test_is_word_in_list_failured():
    assert is_word_in_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"], "mango") == False