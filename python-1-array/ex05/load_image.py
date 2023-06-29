import os
import numpy as np
from PIL import Image


def convert_to_abs(relative_path: str) -> str:
    """Change relative path to absolute path base on script directory

    This function cannot catch file or path exist,
    so you need to handle file existance after this fuction

    Args:
        relative_path (str): relative path string

    Raises:
        TypeError: path must be string
        TypeError: path must be relative

    Returns:
        str: _description_
    """
    # Error handling
    if not isinstance(relative_path, str):
        raise TypeError("path must be string")
    if os.path.isabs(relative_path):
        raise TypeError("path must be relative")

    standard_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(standard_path, relative_path)


def ft_load(path: str) -> np.ndarray:
    """Load image data in numpy array

    Args:
        path (str): file path want to open

    Raises:
        TypeError: path must be string
        FileNotFoundError: no such file to open
        TypeError: file isn't jpeg or jpg
        PIL.UnidentifiedImageError
            : If the image cannot be opened and identified.

    Returns:
        np.ndarray: numpy 3D array representing image data
    """

    # Error handling
    if not isinstance(path, str):
        raise TypeError("path must be string")
    if not os.path.isfile(path):
        raise FileNotFoundError("no such file to open")
    if not path.endswith('.jpeg') and not path.endswith('.jpg'):
        raise TypeError("ft_load only support jpeg or jpg images")

    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
    # : Handling some Errors in PIL
    with Image.open(path) as img:
        np_img = np.array(img)

    print(f'The shape of image is: {np_img.shape}')
    return np_img
