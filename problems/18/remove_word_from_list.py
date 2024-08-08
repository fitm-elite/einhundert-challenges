def remove_word_from_list(words: list[str], word: str) -> list[str]:
    return []

def main():
    removed = remove_word_from_list(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"], "cherry")
    print(removed)

if __name__ == "__main__":
    main()