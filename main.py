from stats import get_book_text, word_reader, count_words, count_char


text = word_reader()
num_words = count_words(text)
print(f"Found {num_words} total words")
num_char = count_char(text)
print(num_char)





     
    