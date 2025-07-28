from stats import get_num_words, get_chars_dict, sorted_list


def main():
    #book_path = "books/frankenstein.txt"
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted = sorted_list(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in chars_sorted:
        character = char_dict["char"]
        count = char_dict["num"]
        print(f"{character}: {count}")
    print("============= END ===============")


# def main():
#     characters = {}
#     book_path = "books/frankenstein.txt"
#     text = get_book_text(book_path)
#     num_words = get_num_words(text)
#     lower_text = text.lower()
#     for character in lower_text:
#         if character in characters:
#             characters[character] += 1
#         else:
#             characters[character] = 1
#     #characters = len(text)
#     print(f"{num_words} words found in the document")
#     #print(f"{characters} characters found in the document")
#     print(characters)

def get_book_text(path):
    with open(path) as f:
        return f.read()

# def count_character(path):
#     lower_text = text.lower()
#     return characters

main()


