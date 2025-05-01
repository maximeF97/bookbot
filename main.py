
import sys
['main.py', 'books/frankenstein.txt']
['main.py', 'books/ mobydick.txt']
['main.py', 'books/prideandprejudice.txt']

def get_book_text(f):
    with open(f) as b:
        return b.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_file = sys.argv[1]
    result = get_book_text(sys.argv[1])
    new_result = char_count(result)
    words = words_counte(result)
    sorted_result = char_organizer(new_result)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found in {book_file}")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_result:
        char = char_dict["char"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")
   

from stats import words_counte
from stats import char_count
from stats import char_organizer

main()



