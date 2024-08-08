from calculate_sum_and_average import calculate_sum_and_average

def test_calculate_sum_and_average(capfd):
    calculate_sum_and_average()
    out, _ = capfd.readouterr()
    
    assert out == "Sum: 102.0\nAverage: 20.4\n"