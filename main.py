import sys
from stats import count_words, count_characters, sort_characters_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    contents = get_book_text(filepath)

    n_words = count_words(contents)
    n_chars_dict = count_characters(contents)

    sorted_list_of_dicts = sort_characters_dict(n_chars_dict)
    print_report(n_words, sorted_list_of_dicts, filepath)

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def print_report(n_words, list_of_dicts, filepath):
    print(f"""
============ BOOKBOT ============
Analyzing book found at {filepath}
----------- Word Count ----------
Found {n_words} total words
--------- Character Count -------
""", end=""
    )

    for d in list_of_dicts:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()