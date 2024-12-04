def count_words(content):
    words = content.split()
    return len(words)


def count_characters(content):
    counted_chars = {}
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

    print(f"--- Begin report of {file_path} ---")
    print(f"Word Count: {count_words(file_contents)}")
    print()
    counted_characters = count_characters(file_contents)
    sorted_characters = dict(
        sorted(counted_characters.items(), key=lambda item: item[1], reverse=True)
    )
    for key, value in sorted_characters.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")


main()
