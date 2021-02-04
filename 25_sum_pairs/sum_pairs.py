def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()

    My test: 5, 2 is the first to meet the goal of 7 but (4, 3) had a smaller index gap
        >>> sum_pairs([5, 1, 8, 2, 4, 3], 7)
        (4, 3)
    """
    # Not sure what they mean by 'and finish before
    # (4, 3) sum to 7, and finish before (5, 2):

    # >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
    # (4, 3)
    # What if:
    # >>> sum_pairs([5, 1, 8, 2, 4, 3], 7)?
    # (5, 2) would 'finish before' (4, 3), heck, (4, 3)
    # was not even evaluate yet.

    # Because of the above ambiguity, my interpretion of
    #  this is to find the pair that reaches the sum with
    #  the smallest index gap between the numbers.
    # >>> sum_pairs([5, 1, 8, 2, 4, 3], 7)?
    # 5,2 may evaluate and reach 7 first (ie, the FIRST set of
    #  numbers to reach the goal of 7, but 4, 3 reached the
    #  goal of 7 as well, and the index gap was 1 -- even though
    #  5,2 evaluated to 7 first.

    idx_max = len(nums)

    if (idx_max > 1):
        # we at least have 2 numbers to check!

        goal_tuples = {}
        while_idx_max = idx_max - 1
        idx = 0
        idx_gap = 0
        min_gap = -1

        while (idx < while_idx_max):
            num1 = nums[idx]
            for num in nums[(idx + 1):]:
                idx_gap += 1
                if (num1 + num == goal):
                    # register the pair, providing a pair does not exist
                    # for this gap (meaning another pair reached the goal first)
                    if (idx_gap not in goal_tuples):
                        goal_tuples[idx_gap] = (num1, num)
                        # check whether index gap is the smallest gap
                        if (min_gap < 0):
                            # first time set
                            min_gap = idx_gap
                        else:
                            if (idx_gap < min_gap):
                                min_gap = idx_gap

            idx += 1
            idx_gap = 0
        # end while

        # anything?
        if (len(goal_tuples) > 0):
            return goal_tuples[min_gap]

    # return when only one number provided in nums or when
    #  no 2 pairs of numbers reach goal.
    return ()
