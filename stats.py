#from main import file_contents

def word_count(file_contents):
    list_words = file_contents.split()
    count = 0
    for i in list_words:
        count +=1
    return count

def ltr_count(file_contents):
    file_content = file_contents.lower()
    item_count = {}
    for i in file_content:
        item_count[i] = item_count.get(i,0) + 1
    return item_count

def sort_char_count(char_dict):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # Fill the list with dictionaries
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    # Define the key function for sorting
    def sort_on(dict_item):
        return dict_item["count"]
    
    # Sort the list
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list
