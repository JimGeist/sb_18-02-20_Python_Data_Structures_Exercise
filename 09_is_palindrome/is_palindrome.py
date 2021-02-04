def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    phrase_lower = phrase.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    phrase_list = [letter.lower()
                   for letter in phrase_lower if letter in letters]
    phrase_list_reverse = phrase_list.copy()
    phrase_list_reverse.reverse()

    if (phrase_list == phrase_list_reverse):
        return True
    else:
        return False
