def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('Springboard Software Engineering Track')
        {'i': 3, 'o': 2, 'a': 3, 'e': 4}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowel_count_out = {}
    if (len(phrase) > 0):
        phrase_lower = phrase.lower()

        #vowel_count_out = {letter: 0 for letter in phrase_lower}
        for letter in phrase_lower:
            if (letter in "aeiou"):
                count = 1 + vowel_count_out.get(letter, 0)
                vowel_count_out[letter] = count

    return vowel_count_out
