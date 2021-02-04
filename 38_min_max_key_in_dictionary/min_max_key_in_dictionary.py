def min_max_keys(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """

    # thinking to change the key list to an array, sort it, then take 0 element
    #  for key_min and -1 for key_max

    if (len(d) > 0):
        key_list = [key for key in d.keys()]
        key_list.sort()
        return (key_list[0], key_list[-1])
    else:
        return ()
