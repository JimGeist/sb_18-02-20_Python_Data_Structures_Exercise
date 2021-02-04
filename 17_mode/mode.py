def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # mode_out will hold the number that occurred the most
    mode_out = ""
    # greatest_frequency will hold the largest total times a number occured.

    greatest_frequency = 0
    num_frequency = {num: 0 for num in nums}
    for num in nums:
        num_frequency[num] += 1
        # did the amount of times num occur exceed the amount in greatest_frequency?
        if (num_frequency[num] >= greatest_frequency):
            # yes, we have a new most common number
            mode_out = num

    return mode_out
