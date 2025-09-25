import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_reader():
    book_text = get_book_text(file_path)
    return book_text

def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_char(book_text):
    characters = {}
    for ch in book_text.lower():
        if ch in characters:
            characters[ch] += 1
        else:
            characters[ch] = 1
    return characters

def sorted_char(char_counts):
    def get_num(items):
        return items["num"]
    chara_list = []
    for ch, count in char_counts.items():
        chara_list.append({"char": ch, "num": count})
    chara_list.sort(reverse=True, key=get_num)
    return chara_list
    
               
