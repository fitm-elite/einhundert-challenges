from palindrome_partitioning_with_minimum_cuts import palindrome_partitioning_with_minimum_cuts

def test_palindrome_partitioning_with_minimum_cuts():
    assert palindrome_partitioning_with_minimum_cuts("aab") == 1
    assert palindrome_partitioning_with_minimum_cuts("abccba") == 0
    assert palindrome_partitioning_with_minimum_cuts("aabbc") == 2