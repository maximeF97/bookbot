
def get_book_text(f):
    with open(f) as b:
        return b.read()
    
def main():
    result = get_book_text("books/frankenstein.txt")
    new_result = char_count(result)
    words = words_counte(result)
    sorted_result = char_organizer(new_result)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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



