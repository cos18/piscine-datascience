import numpy as np


def is_ndarray_from_pil(target: np.ndarray) -> bool:
    """check if array is from PIL Image class

    Args:
        target (np.ndarray): check array

    Returns:
        bool: if array is from PIL Image class
    """
    if not isinstance(target, np.ndarray):
        return False
    if len(target.shape) != 3:
        return False
    return np.issubdtype(target.dtype, np.uint8)


def ft_invert(origin: np.ndarray) -> np.ndarray:
    if not is_ndarray_from_pil(origin):
        raise TypeError("origin must be numpy 3D uint8 ndarray")
    result = np.empty(origin.shape, dtype=origin.dtype)
    for x in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            for c in range(origin.shape[2]):
                result[x, y, c] = 255 - result[x, y, c]
    return result


def ft_red(origin: np.ndarray) -> np.ndarray:
    pass


def ft_green(origin: np.ndarray) -> np.ndarray:
    pass


def ft_blue(origin: np.ndarray) -> np.ndarray:
    pass


def ft_grey(origin: np.ndarray) -> np.ndarray:
    pass
