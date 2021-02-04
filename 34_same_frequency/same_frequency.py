def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """
    num1_list = [digit for digit in str(num1)]
    num2_list = [digit for digit in str(num2)]

    if (len(num1_list) == len(num2_list)):
        num1_list.sort()
        num2_list.sort()
        if (num1_list == num1_list):
            # num1 and num2 both have the same digits, just in different order
            return True
        else:
            # the lists have the same length, but different digits
            return False

    else:
        # different number of digits
        return False
