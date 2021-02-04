def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    the_truth_the_whole_truth_and_nothing_but_truth = [
        istruthy for istruthy in lst if (not(not(istruthy)))]

    return the_truth_the_whole_truth_and_nothing_but_truth
