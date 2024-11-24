def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        report(book_path, count_words(file_contents), count_chars(file_contents))


def report(book_path, count_words, count_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words} words found in the document")
    print("\n")
    for char in count_chars:
        print(f"The {char} character was found {count_chars[char]} times")
    return


def count_chars(text):
    chars = {}
    for c in text.lower():
        if c not in chars:
            chars[c] = 1
        else:
            chars[c] += 1
    return chars

def count_words(text):
    words: list = text.split()
    return len(words)

if __name__ == "__main__":
    main()
