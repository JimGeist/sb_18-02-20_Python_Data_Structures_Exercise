def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    # letter count via list comprehension
    letter_lower = letter.lower()
    word_lower = word.lower()
    if (letter_lower in word_lower):
        letter_list = [char for char in word_lower if char == letter_lower]
        return len(letter_list)

    else:
        return 0
