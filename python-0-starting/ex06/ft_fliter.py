def ft_filter(func, sequence):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""

    # check sequence is iterable -> if it isn't, throw TypeError
    iter(sequence)
    return [item for item in sequence if (func(item) if func else item)]
