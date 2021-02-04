def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    swap_test = {to_swap.lower(), to_swap.upper()}

    phrase_flip = [
        letter.swapcase() if letter in swap_test else letter for letter in phrase]

    return "".join(phrase_flip)
