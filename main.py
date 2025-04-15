import sys
from stats import get_num_words, get_character_count, get_sorted_dict

#['main.py', 'books/frankenstein.txt']

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        word_count = get_num_words(text)
        char_count = get_character_count(text)
        sorted_report = get_sorted_dict(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for line in sorted_report:
            print(line)

main()