from find_multiples_of_three_and_four import find_multiples_of_three_and_four

def test_find_multiples_of_three():
    assert find_multiples_of_three_and_four(start=10, end=50) == [12, 24, 36, 48]