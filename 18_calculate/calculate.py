def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """

    C_ADD = "add"
    C_SUB = "subtract"
    C_MULT = "multiply"
    C_DIV = "divide"
    valid_operations = {C_ADD, C_SUB, C_MULT, C_DIV}
    result = 0

    operation_lower = operation.lower()
    if (operation_lower in valid_operations):
        if (operation_lower == C_ADD):
            result = a + b
        elif (operation_lower == C_SUB):
            result = a - b
        elif (operation_lower == C_MULT):
            result = a * b
        else:
            # opeation is divide via process of elimination
            result = a / b

        if make_int:
            # cast as an integer
            result = int(result)

        return f"{message} {result}"

    else:
        return None
