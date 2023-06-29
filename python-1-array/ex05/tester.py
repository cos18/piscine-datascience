from load_image import ft_load, convert_to_abs
from pimp_image import ft_invert, ft_red, ft_blue, ft_green, ft_grey
from PIL import Image


def main():
    """
    Test code
    """

    try:
        array = ft_load(convert_to_abs("../landscape.jpeg"))
        print(array)
        Image.fromarray(ft_invert(array)).show()
        Image.fromarray(ft_red(array)).show()
        Image.fromarray(ft_green(array)).show()
        Image.fromarray(ft_blue(array)).show()
        Image.fromarray(ft_grey(array)).show()
        print(ft_invert.__doc__)
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
