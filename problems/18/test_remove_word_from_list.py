from remove_word_from_list import remove_word_from_list

def test_remove_word_from_list():
    assert remove_word_from_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"], "cherry") == ["apple", "banana", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]