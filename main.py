from stats import count_words, count_chars

def main():
    filepath = "./books/frankenstein.txt"
    contents = get_book_text(filepath)

    n_words = count_words(contents)
    print(f"{n_words} words found in the document")

    char_frequency = count_chars(contents)
    print(char_frequency)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents




if __name__ == "__main__":
    main()