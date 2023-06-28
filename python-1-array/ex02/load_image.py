import os
import numpy as np
from PIL import Image


def ft_load(path: str) -> np.ndarray:
    if not os.path.exists(path):
        raise FileNotFoundError("no such file to open")
    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
    # : Handling Error
    with Image.open(path) as img:
        np_img = np.array(img)

    print(f'The shape of image is: {np_img.shape}')
    return np_img
