from stats import word_count
from stats import ltr_count
from stats import sort_on

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
# def word_count(file_contents):
#    list_words = file_contents.split()
#    count = 0
#    for i in list_words:
#        count +=1
#    return count

def main():
    output = get_book_text("books/frankenstein.txt")
    wc = word_count(output)
    print(f"{wc} words found in the document")
    item_count = ltr_count(output)
    print(item_count)
    print(letters.isalpha())
main()
