def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    # make a list of vowels then start popping them off the list
    #  as a vowel is encountered in the string.

    VOWELS = "aAeEiIoOuU"
    s_vowels = [letter for letter in s if (letter in VOWELS)]
    s_out = []

    for letter in s:
        if (letter in VOWELS):
            s_out.append(s_vowels.pop())
        else:
            s_out.append(letter)

    return "".join(s_out)
