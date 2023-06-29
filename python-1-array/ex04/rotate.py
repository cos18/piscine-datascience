import numpy as np
from PIL import Image
from load_image import ft_load, convert_to_abs


def cut_square(
        origin: np.ndarray,
        start_x: int,
        start_y: int,
        length: int
        ) -> np.ndarray:
    """Cut image to square

    Args:
        origin (np.ndarray): source data to cut
        start_x (int): left upper point x (depend on height) value
        start_y (int): left upper point y (depend on width) value
        length (int): square length of result image data

    Raises:
        TypeError: image must be 3D ndarray, cut parameter must be integer
        IndexError: cut parameter must fit in origin shape

    Returns:
        np.ndarray: cut square image data
    """

    # Error handling
    if not isinstance(origin, np.ndarray) or len(origin.shape) != 3:
        raise TypeError("origin must be numpy 3D ndarray")
    if (not isinstance(start_x, int) or
        not isinstance(start_y, int) or
            not isinstance(length, int)):
        raise TypeError("cut parameter must be integer")
    origin_shape = origin.shape
    end_x = start_x + length
    end_y = start_y + length
    if not (0 <= start_x < origin_shape[0] and
            0 <= end_x < origin_shape[0] and
            0 <= start_y < origin_shape[1] and
            0 <= end_y < origin_shape[1]):
        raise IndexError("cut parameter must fit in origin shape")

    return origin[start_x:end_x, start_y:end_y, ]


def transpose_image(origin: np.ndarray) -> np.ndarray:
    """Transpose square image

    Args:
        origin (np.ndarray): source data to transpose

    Raises:
        TypeError: origin must be 3D square numpy ndarray

    Returns:
        np.ndarray: transposed data
    """
    # Error handling
    if not isinstance(origin, np.ndarray) or len(origin.shape) != 3:
        raise TypeError("origin must be numpy 3D ndarray")
    if origin.shape[0] != origin.shape[1]:
        raise TypeError("origin isn't square size")

    result = np.empty(origin.shape, dtype=origin.dtype)
    for x in range(origin.shape[0]):
        for y in range(origin.shape[1]):
            result[x, y] = origin[y, x]
    return result


def main():
    """
    load the image "animal.jpeg",
    cut a square part from it
    and transpose it
    """

    try:
        origin = ft_load(convert_to_abs("../animal.jpeg"))
        square = cut_square(origin, 100, 450, 400)
        print(f"The shape of image is: {square.shape}")
        print(square)
        transpose = transpose_image(square)
        print(f"New shape after Transpose: {transpose.shape}")
        print(transpose)
        Image.fromarray(transpose).show()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
