import pytest

from collect_unique_words import collect_unique_words

def test_collect_unique_words():
    uniques = collect_unique_words()
    
    uniques_len = len(uniques)
    assert uniques_len == 5
    
    unique_keys = dict.fromkeys(uniques, 0)
    for word in uniques:
        if word in unique_keys:
            unique_keys[word] += 1
            
    for key in unique_keys:
        assert unique_keys[key] == 1
        