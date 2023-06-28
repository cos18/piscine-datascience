import numpy as np


def give_bmi(
        height: list[int | float],
        weight: list[int | float]
        ) -> list[int | float]:
    """Give multiple BMI values base on height and weight list

    Args:
        height (list[int | float]): height number list
        weight (list[int | float]): weight number list

    Raises:
        TypeError: height or weight value is not int or float
        LookupError: size of height and weight are different or not 1D

    Returns:
        list[int | float]: BMI values
    """
    # Error handling
    if (not isinstance(height, list)) or (not isinstance(weight, list)):
        raise TypeError("height or weight isn't list")
    try:
        height = np.array(height, dtype='float64')
        weight = np.array(weight, dtype='float64')
    except ValueError:
        raise TypeError("list item values isn't integer or float")
    if len(height.shape) != 1 or len(weight.shape) != 1:
        raise LookupError("height or weight list isn't 1D")
    if height.shape != weight.shape:
        raise LookupError("height and weight list length isn't same")

    # Calculate BMI
    return (weight / (height ** 2)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Check bmi value with the limit

    Args:
        bmi (list[int | float]): BMI number list
        limit (int): Limit which compare to BMI

    Raises:
        TypeError: BMI isn't int or float, or limit isn't int
        LookupError: BMI isn't 1D

    Returns:
        list[bool]: Bool value if BMI is above than limit
    """
    # Error handling
    if not isinstance(bmi, list):
        raise TypeError("height or weight isn't list")
    if not isinstance(limit, int):
        raise TypeError("limit values isn't integer")
    try:
        bmi = np.array(bmi, dtype='float64')
    except ValueError:
        raise TypeError("list item values isn't integer or float")
    if len(bmi.shape) != 1:
        raise LookupError("bmi list isn't 1D")

    return [b > limit for b in bmi]
