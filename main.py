import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    file_path = sys.argv[1]


from stats import get_book_text, word_reader, count_words, count_char, sorted_char

text = get_book_text(file_path)
num_words = count_words(text)
num_char = count_char(text)
sorted_list = sorted_char(num_char)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {file_path}...")
print("----------- Word Count ----------")
print(f"Found {num_words} total words")
print("--------- Character Count -------")
for item in sorted_list:
    ch = item["char"]
    if not ch.isalpha():
        continue
    print(f"{ch}: {item['num']}")
print("============= END ===============")




     
    