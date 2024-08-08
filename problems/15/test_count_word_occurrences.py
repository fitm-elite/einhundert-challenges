from count_word_occurrences import count_word_occurrences

def test_count_word_occurrences():
    assert count_word_occurrences(["apple", "banana", "apple", "orange", "banana", "apple"]) == {"apple": 3, "banana": 2, "orange": 1}
