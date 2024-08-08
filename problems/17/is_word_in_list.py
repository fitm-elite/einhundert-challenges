def is_word_in_list(words_list: list[str], search_term: str) -> bool:
    return False

def main():
    matched = is_word_in_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"], "cherry")
    print(matched)
    
    matched = is_word_in_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"], "mango")
    print(matched)

if __name__ == "__main__":
    main()