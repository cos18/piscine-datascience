def ft_filter(func, sequence):
    """Return those items of sequence for which function(item) is true.

    Args:
        func (function or None):
            Decide which item are return. If None, check item itself.
        sequence (iterable):
            Iterable that contain origin items.

    Returns:
        list, tuple, or string:
            If sequence is a tuple or string, return the same type,
            else return a list.

    Raises:
        TypeError:
            An error occurred function isn't callable
            or sequence is not iterable.
    """

    # check sequence is iterable -> if it isn't, throw TypeError
    iter(sequence)
    if isinstance(sequence, str):
        return str(s for s in sequence if (func(s) if func else s))
    if type(sequence) is tuple:
        return tuple(s for s in sequence if (func(s) if func else s))
    return [s for s in list(sequence) if (func(s) if func else s)]
