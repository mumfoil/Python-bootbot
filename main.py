from stats import num_word_count, num_char, get_char_num, dict_sorted
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

sys.argv
def get_book_text(filepath):
    with open(filepath, encoding ="utf-8") as f:
        return f.read()


def main():
    path = sys.argv[1]
    text = get_book_text(path)
    count = num_word_count(text)
    chardict = num_char(text)
    sorted_char = dict_sorted(chardict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
main()


