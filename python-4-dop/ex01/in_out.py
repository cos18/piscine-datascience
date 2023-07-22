def square(x):
    """calculate square

    Args:
        x (number): input number

    Returns:
        number: calculated number
    """
    return x * x


def pow(x):
    """calculate power

    Args:
        x (number): input number

    Returns:
        number: calculated number
    """
    return x ** x


def outer(x, function):
    """making function object that doing function

    Args:
        x (Any): using value
        function (function): doing function

    Returns:
        function object
    """
    count = x

    def inner():
        """inner function that returns

        Returns:
            Any: calculated value
        """
        # https://docs.python.org/3/reference/simple_stmts.html#nonlocal
        nonlocal count
        count = function(count)
        return count
    return inner
