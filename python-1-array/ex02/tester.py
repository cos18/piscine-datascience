from load_image import ft_load, convert_to_abs


def main():
    """
    Test function of this exercise
    """

    print(ft_load(convert_to_abs("../landscape.jpeg")))
    try:
        ft_load(convert_to_abs("file_not_exist.jpeg"))
    except FileNotFoundError as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
