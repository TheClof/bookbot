def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    #print(f"char: {lowered}, num: {chars}")
    return chars
    
def sorted_list(chars_dict):
    char_list = []
    for char, count in chars_dict.items():
        if char.isalpha():
            char_dict = {"char": char, "num": count}
            char_list.append(char_dict)
    char_list.sort(reverse=True, key=sort_on)  
    return char_list

def sort_on(char_list):
    return char_list["num"]


    # Add a new function to your stats.py file that takes the dictionary of characters and 
    # their counts and returns a sorted list of dictionaries.
    #     Each dictionary should have two key-value pairs: one for the character itself and 
    #     one for that character's count (e.g. {"char": "b", "num": 4868}).
    #     Sort the list from greatest to least by the count.
    #     The .sort() method will be helpful here (see the example).
    # Import and call the function in main.py, and capture the result.
    # Print the report to the console as shown above. If the character is not an 
    # alphabetical character (using the .isalpha() method), just skip it.
