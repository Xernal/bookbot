import sys

from stats import wordcount
from stats import charactercount
from stats import sort_on
from stats import sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

booklink = sys.argv[1]

wordcount(booklink)
charactercount(booklink)
sort_dict(booklink)

no_of_words = wordcount(booklink)
temp_sort_list = sort_dict(booklink)



print("============ BOOKBOT ============")
print(f"Analyzing book found at {booklink}...")
print("----------- Word Count ----------")
print(f"Found {no_of_words} total words")
print("--------- Character Count -------")

for pair in temp_sort_list:
    print(f"{pair['char']}: {pair['num']}")