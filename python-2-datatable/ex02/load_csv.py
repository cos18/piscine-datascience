import os
import pandas as pd
from pandas.core.frame import DataFrame


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


def load(path: str) -> DataFrame:
    """Load csv data in pandas DataFrame

    Args:
        path (str): file path want to open

    Raises:
        TypeError: path must be string
        FileNotFoundError: no such file to open
        TypeError: file isn't jpeg or jpg
        Handling some Errors in Pandas:
            https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    Returns:
        DataFrame: two-dimensional data structure with labeled axes
    """

    # Error handling
    if not isinstance(path, str):
        raise TypeError("path must be string")
    if not os.path.isfile(path):
        raise FileNotFoundError("no such file to open")
    if not path.endswith('.csv'):
        raise TypeError("load function only support csv file")
    result = pd.read_csv(path)
    print(f'Loading dataset of dimensions {result.shape}')
    return result
