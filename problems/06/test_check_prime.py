from check_prime import check_prime

def test_check_prime_passed():
    assert check_prime(17) == "is prime"

def test_check_prime_failured():
    assert check_prime(18) == "is not prime"