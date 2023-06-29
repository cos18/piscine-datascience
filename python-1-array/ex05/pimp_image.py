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
    if not np.issubdtype(target.dtype, np.uint8):
        return False
    for ele in np.nditer(target.flatten()):
        if ele < 0 or 255 < ele:
            return False
    return True


def ft_invert(origin: np.ndarray) -> np.ndarray:
    """Invert image

    Args:
        origin (np.ndarray): origin image data

    Raises:
        TypeError: origin must be numpy 3D uint8 ndarray

    Returns:
        np.ndarray: inverted image
    """
    if not is_ndarray_from_pil(origin):
        raise TypeError("origin must be numpy 3D uint8 ndarray")
    result = origin.copy()
    for x in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            for c in range(origin.shape[2]):
                result[x, y, c] = 255 - result[x, y, c]
    return result


def ft_red(origin: np.ndarray) -> np.ndarray:
    """Red filter image

    Args:
        origin (np.ndarray): origin image data

    Raises:
        TypeError: origin must be numpy 3D uint8 ndarray

    Returns:
        np.ndarray: red filtered image
    """
    if not is_ndarray_from_pil(origin):
        raise TypeError("origin must be numpy 3D uint8 ndarray")
    result = origin.copy()
    for x in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            result[x, y, 1] = 0
            result[x, y, 2] = 0
    return result


def ft_green(origin: np.ndarray) -> np.ndarray:
    """Green filter image

    Args:
        origin (np.ndarray): origin image data

    Raises:
        TypeError: origin must be numpy 3D uint8 ndarray

    Returns:
        np.ndarray: red filtered image
    """
    if not is_ndarray_from_pil(origin):
        raise TypeError("origin must be numpy 3D uint8 ndarray")
    result = origin.copy()
    for x in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            result[x, y, 0] = 0
            result[x, y, 2] = 0
    return result


def ft_blue(origin: np.ndarray) -> np.ndarray:
    """Blue filter image

    Args:
        origin (np.ndarray): origin image data

    Raises:
        TypeError: origin must be numpy 3D uint8 ndarray

    Returns:
        np.ndarray: blue filtered image
    """
    if not is_ndarray_from_pil(origin):
        raise TypeError("origin must be numpy 3D uint8 ndarray")
    result = origin.copy()
    for x in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            result[x, y, 0] = 0
            result[x, y, 1] = 0
    return result


def ft_grey(origin: np.ndarray) -> np.ndarray:
    """Greyscale image

    Args:
        origin (np.ndarray): origin image data

    Raises:
        TypeError: origin must be numpy 3D uint8 ndarray

    Returns:
        np.ndarray: grayscale image
    """
    if not is_ndarray_from_pil(origin):
        raise TypeError("origin must be numpy 3D uint8 ndarray")
    result = np.empty(origin.shape[:2], dtype=np.uint8)
    for x in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            result[x, y] = int(origin[x, y].sum() / 3)
    return result
