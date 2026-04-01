import sys
from stats import get_number_of_words, get_char_frequency, chars_dict_to_sorted_list


def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()


def main():

    args = sys.argv

    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = args[1]
    



    contents = get_book_text(file_path)
    num_words = get_number_of_words(contents)
    char_freq = get_char_frequency(contents)
    sorted_chars_freq_list = chars_dict_to_sorted_list(char_freq)
    print("=============== BOOKBOT ===============")
    print(f"Analyzing book found at {file_path}")
    print("--------------- Word Count -------------")
    print(f"Found {num_words} total words")
    print("------------- Characher Count -----------")

    for char_freq_obj in sorted_chars_freq_list:
        char = char_freq_obj['char']
        char_count = char_freq_obj['num']
        print(f"{char}: {char_count}")

main()
