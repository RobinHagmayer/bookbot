def get_num_words(content: str) -> int:
    words = content.split()
    return len(words)


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
