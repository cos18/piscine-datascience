import numpy as np
from PIL import Image
from load_image import ft_load, convert_to_abs


def zoom_image(
        origin: np.ndarray,
        start_x: int,
        start_y: int,
        width: int,
        height: int
        ) -> np.ndarray:
    """Zoom image

    Args:
        origin (np.ndarray): source data to zoom
        start_x (int): left upper point x (depend on height) value
        start_y (int): left upper point y (depend on width) value
        width (int): width of result image data
        height (int): width of result image data

    Raises:
        TypeError: image must be ndarray, zoom parameter must be integer
        IndexError: zoom parameter must fit in origin shape

    Returns:
        np.ndarray: zoom image data
    """

    # Error handling
    if not isinstance(origin, np.ndarray) or len(origin.shape) != 3:
        raise TypeError("origin must be numpy 3D ndarray")
    if (not isinstance(start_x, int) or
        not isinstance(start_y, int) or
        not isinstance(width, int) or
            not isinstance(height, int)):
        raise TypeError("zoom parameter must be integer")
    origin_shape = origin.shape
    end_x = start_x + height
    end_y = start_y + width
    if not (0 <= start_x < origin_shape[0] and
            0 <= end_x < origin_shape[0] and
            0 <= start_y < origin_shape[1] and
            0 <= end_y < origin_shape[1]):
        raise IndexError("zoom parameter must fit in origin shape")

    return origin[start_x:end_x, start_y:end_y, ]


def main():
    """
    load the image "animal.jpeg",
    print some information about it
    and display it after "zooming".
    """

    try:
        origin = ft_load(convert_to_abs("../animal.jpeg"))
        zoom = zoom_image(origin, 100, 450, 400, 400)
        print(f"New shape after slicing: {zoom.shape}")
        print(zoom)
        Image.fromarray(zoom).show()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
