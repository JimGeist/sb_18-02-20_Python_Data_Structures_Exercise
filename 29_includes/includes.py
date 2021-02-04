def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    if (len(collection) > 0):
        #print(f"collection {collection} is a {type(collection)}")
        if(isinstance(collection, dict)):
            for key in collection.keys():
                if (collection[key] == sought):
                    return True
        elif(isinstance(collection, set) or isinstance(collection, str)):
            if (sought in collection):
                return True
        elif(isinstance(collection, tuple)):
            if (collection.count(sought) > 0):
                return True
        elif(isinstance(collection, list)):
            if (start == None):
                idx_start = 0
            else:
                idx_start = start

            if (sought in collection[idx_start:]):
                return True

    return False
