def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_reader():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    return book_text

def count_words(book_text):
    words = book_text.split()
    return len(words)