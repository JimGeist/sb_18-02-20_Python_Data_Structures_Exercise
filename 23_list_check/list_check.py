def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    if (len(lst) > 0):
        for item in lst:
            if (isinstance(item, list) == False):
                # end the check when we encounter a false
                return False
        # we checked the entire list and all items in lst are lists.
        return True
    else:
        return False
