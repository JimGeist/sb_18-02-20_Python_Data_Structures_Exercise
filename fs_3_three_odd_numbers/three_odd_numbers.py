def three_odd_numbers(nums):
    """Is the sum of any 3 consecutive (consecutive, not sequential) numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    max_len = len(nums)
    if (max_len > 2):
        # we have at least 3 numbers. Let's begin.
        # max_len will control end of the loop. We need to fix the max_len so we
        #  only loop while there are three consecutive numbers to sum
        max_len = max_len - 2
        idx = 0
        total_of_three = 0
        while (idx < max_len):
            total_of_three = nums[idx] + nums[idx + 1] + nums[idx + 2]
            if (total_of_three % 2 == 1):
                # the total of 3 consecutive numbers is odd
                return True

            idx += 1

    return False
