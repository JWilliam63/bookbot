def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_count = get_character_count(text)
    print(f"{num_words} words found in the document")
    print(f"{character_count} were found in the document")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_character_count(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return(char_counts)
main()
