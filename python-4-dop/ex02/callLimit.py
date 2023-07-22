def callLimit(limit: int):
    """Decorator that blocks its execution above a limit

    Args:
        limit (int): limit function call

    Returns:
        function object
    """
    count = 0

    def callLimiter(function):
        """Limiter function
        """
        def limit_function(*args, **kwds):
            """main limit function
            """
            nonlocal count
            if count == limit:
                print("Error:", function, "call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function
    return callLimiter
