def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1

    If the list is empty, return 1.

        >>> multiply_even_numbers([])
        1

    """

    evens_product_out = 1
    nums_even = [num for num in nums if num % 2 == 0]
    if (len(nums_even) > 0):
        for num in nums_even:
            evens_product_out *= num

    return evens_product_out
