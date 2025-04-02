import sys

from stats import count_characters, get_num_words


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path) as f:
        file_contents = f.read()

    num_words = get_num_words(file_contents)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    counted_characters = count_characters(file_contents)
    sorted_characters = dict(
        sorted(counted_characters.items(), key=lambda item: item[1], reverse=True)
    )
    for key, value in sorted_characters.items():
        print(f"{key}: {value}")
    print("============= END ===============")


main()
