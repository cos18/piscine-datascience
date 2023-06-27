def count_in_list(data, target) -> int:
    """count how many target appear in data

    Args:
        data (iterable): iterable data. print error log if isn't iterable
        target (object - any): count target

    Returns:
        int: count value
    """
    try:
        iter(data)
    except TypeError as err:
        print(f"{type(err).__name__} : {err}")
        return -1
    result = 0
    for d in data:
        if d == target:
            result += 1
    return result


def main():
    """
    Init package
    """
    __all__ = ['count_in_list']
    __all__


if __name__ == "__main__":
    main()
