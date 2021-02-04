def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    command_valid = ("add", "remove")
    location_valid = ("beginning", "end")

    if ((command.lower() in command_valid) and (location.lower() in location_valid)):
        # commands and location are good
        if (command.lower() == "add"):
            # command is add
            if (location.lower() == "beginning"):
                # add to beginning of list
                lst.insert(0, value)
            else:
                # add to end
                lst.append(value)
            return lst
        else:
            # command is remove
            if (location.lower() == "beginning"):
                # remove from beginning of list
                return lst.pop(0)
            else:
                # remove from end
                return lst.pop()
    else:
        # Invalid commands or locations should return None
        return None
