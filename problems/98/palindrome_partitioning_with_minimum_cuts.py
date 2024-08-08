def palindrome_partitioning_with_minimum_cuts(s: str) -> int:
    pass

def main():
    s = "aab"
    print(palindrome_partitioning_with_minimum_cuts(s)) # 1
    
    s = "abccba"
    print(palindrome_partitioning_with_minimum_cuts(s)) # 0
    
    s = "aabbc"
    print(palindrome_partitioning_with_minimum_cuts(s)) # 2