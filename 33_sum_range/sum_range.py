def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum = 0
    if (start < len(nums)):
        # calculate end of splice so we can use a common
        #  for to calculate the sum, no matter what was entered for end.
        if (end == None):
            slice_stop = len(nums) + 1
        else:
            slice_stop = end + 1

        for num in nums[start:slice_stop]:
            sum += num

    return sum
