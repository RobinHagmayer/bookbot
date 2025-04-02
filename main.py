from stats import get_num_words


def count_characters(content: str) -> dict[str, int]:
    counted_chars: dict[str, int] = {}
    for char in content.strip():
        if not char.isalpha():
            continue
        char = char.lower()
        if char not in counted_chars:
            counted_chars[char] = 1
            continue
        counted_chars[char] += 1

    return counted_chars


def main():
    file_path = "books/frankenstein.txt"

    with open(file_path) as f:
        file_contents = f.read()

    num_words = get_num_words(file_contents)
    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document")
    print()
    counted_characters = count_characters(file_contents)
    sorted_characters = dict(
        sorted(counted_characters.items(), key=lambda item: item[1], reverse=True)
    )
    for key, value in sorted_characters.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


main()
