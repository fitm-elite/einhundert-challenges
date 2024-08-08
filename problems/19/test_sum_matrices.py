from sum_matrices import sum_matrices

def test_sum_matrices():
    assert sum_matrices([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [[4, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 1]]) == [[5, 5, 5, 5], [9, 9, 9, 9], [13, 13, 13, 13]]