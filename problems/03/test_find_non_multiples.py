from find_non_multiples import find_non_mutiples

def test_find_multiples_of_three():
    assert find_non_mutiples(start=10, end=25) == [11, 13, 17, 19, 23]