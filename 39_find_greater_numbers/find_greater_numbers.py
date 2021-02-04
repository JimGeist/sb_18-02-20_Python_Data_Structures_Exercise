def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    idx_start = 0
    max_times = len(nums)
    nbr_of_times_out = 0

    while (idx_start < max_times):
        num_test = nums[idx_start]
        for num in nums[idx_start:]:
            if num_test < num:
                nbr_of_times_out += 1

        idx_start += 1

    return nbr_of_times_out
