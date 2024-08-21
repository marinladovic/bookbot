def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(get_character_count(text))

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(contents):
    return len(contents.split())

def get_character_count(text):
    lowered_string = text.lower()
    char_count_dict = {}
    for char in lowered_string:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

main()