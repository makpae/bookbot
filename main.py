from stats import word_count, ltr_count, sort_char_count 
import sys
# Import your new sorting function

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    word_count_result = word_count(text)
    char_count_dict = ltr_count(text)

    # Get sorted list of character dictionaries
    sorted_chars = sort_char_count(char_count_dict)
    
    # Print the report according to the specified format
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count_result} total words")
    print("--------- Character Count -------")
    
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()
