def mean(args):
    """Calculate mean

    Args:
        args (List[int, float]): args list

    Returns:
        Union[int, float]: mean result
    """
    return sum(args) / len(args)


def median(args):
    """Calculate median

    Args:
        args (List[int, float]): args list

    Returns:
        Union[int, float]: median result
    """
    if len(args) % 2:
        return args[len(args) // 2]
    return (args[len(args) // 2] + args[len(args) // 2 - 1]) / 2


def quartile(args):
    """Calculate quartile
    There is no universal agreement on selecting the quartile values
    for discrete distributions.
    This function implements Method 2 in wikipedia.
    https://en.wikipedia.org/wiki/Quartile

    Args:
        args (List[int, float]): args list

    Returns:
        Union[int, float]: mean result
    """
    mid = len(args) // 2
    if len(args) % 2:
        return [median(args[:mid + 1]), median(args[mid:])]
    return [median(args[:mid]), median(args[mid:])]


def var(args):
    """Calculate variance

    Args:
        args (List[int, float]): args list

    Returns:
        Union[int, float]: variance result
    """
    m = mean(args)
    return sum([(a - m) ** 2 for a in args]) / len(args)


def std(args):
    """Calculate standard deviation

    Args:
        args (List[int, float]): args list

    Returns:
        Union[int, float]: standard deviation result
    """
    return var(args)**.5


def ft_statistics(*args, **kwargs):
    """Calculate basic statistics value about args

    Args:
        args (Any): Values want to calcuate stat info
        kwargs (Any): target stat name
    """
    defined_method = ['mean', 'median', 'quartile', 'std', 'var']
    args = list(filter(
        lambda val: type(val) == int or type(val) == float,
        args
    ))
    args.sort()
    for value in kwargs.values():
        if value not in defined_method:
            continue
        if not len(args):
            print('ERROR')
            continue
        print(f'{value} : {eval(value)(args)}')
