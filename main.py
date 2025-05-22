import sys
from stats import get_num_words, get_char_count
from sys import argv

def get_boot_text():

    with open(argv[1]) as f:
        # f is a file object
        file_contents = f.read()


    return file_contents
    
def main():
    """
    Main function to execute the script.    
    """
    print("============ BOOKBOT ============\n")
    print("Analyzing book found at books/frankenstein.txt...\n")
    print("----------- Word Count ----------\n")



    file_contents = get_boot_text()


    num_words = get_num_words(file_contents)
    print()
    print(f"Found {num_words} total words\n")
    print("----------- Character Count ----------\n")

    char_count = get_char_count(file_contents)
    # Sort characters by count, highest to lowest
    for char, count in sorted(char_count.items(), key=lambda item: item[1], reverse=True):
        print(f"{char}: {count}")

    print("============= END ===============")

if len(argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()
