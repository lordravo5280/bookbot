import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_books>")
    sys.exit(1)

from stats import num_words, num_characters, sorted_list

def main():
    try:
        with open(sys.argv[1]) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{sys.argv[1]}' was not found.")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at '{sys.argv[1]}'...")

    print("----------- Word Count ----------")
    print(f"Found {num_words(file_contents)} total words")

    print("--------- Character Count -------")
    sorted_chars = sorted_list(num_characters(file_contents))

    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            count = char_dict["count"]
            print(f"{char}: {count}")
    print("============= END ===============")
main()