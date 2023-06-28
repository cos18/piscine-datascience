import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice family and compare shape

    Args:
        family (list): 2D list to slice
        start (int): start index
        end (int): end index

    Raises:
        TypeError: args type are different or can't fit 2D list

    Returns:
        list: slicing list
    """
    if not isinstance(family, list):
        raise TypeError("family values isn't list")
    if (not isinstance(start, int)) or (not isinstance(end, int)):
        raise TypeError("start or end values isn't integer")
    try:
        family = np.array(family)
    except ValueError:
        raise TypeError("family list isn't fit to shape")
    if len(family.shape) != 2:
        raise TypeError("family isn't 2D")

    print(f"My shape is : {family.shape}")
    family = family[start:end, ]
    print(f"My new shape is : {family.shape}")
    return family.tolist()
