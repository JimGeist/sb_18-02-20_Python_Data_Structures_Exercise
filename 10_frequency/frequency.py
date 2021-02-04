def frequency(lst, search_term):
    """Return frequency of term in lst.

        >>> frequency([1, 4, 3, 4, 4], 4)
        3

        >>> frequency([1, 4, 3], 7)
        0

        >>> frequency([], 7)
        0
    """

    if (search_term in lst):
        freq_list = [nbr for nbr in lst if nbr == search_term]
        return len(freq_list)
    else:
        return 0
