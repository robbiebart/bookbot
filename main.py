import sys
from stats import get_num_words
from stats import character_count
from stats import sort_dictionaries

def main():
    if len(sys.argv) > 1: 
        path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(path)
    
    char_count = character_count(book_text)
    sorted_dictionaries = sort_dictionaries(char_count)
    print_report(sorted_dictionaries, book_text, path)

def print_word_count(book_text):
    word_count = get_num_words(book_text)
    print(f"Found {word_count} total words")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
    
def print_dictionary(sorted_dictionary):
    for entry in sorted_dictionary:
        print(f"{entry["char"]}: {entry["num"]}")

def print_report(sorted_dictionary, book_text, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print_word_count(book_text)
    print("--------- Character Count -------")
    print_dictionary(sorted_dictionary)
    print("============= END ===============")
    

main()