def divide_nums(num1, num2):

    """
    Divide two numbers.

    :param float num1: The numerator.
    :param float num2: The denominator (must be non-zero).

    :returns: The result of dividing `num1` by `num2`.
    :rtype: float
    """
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    answer = num1 / num2
    return answer
