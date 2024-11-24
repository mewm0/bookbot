def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        print(count_chars(file_contents))
               

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
