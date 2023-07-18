from ft_calculator import calculator


def test():
    """Test function
    """
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5

    try:
        v3 / 0
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == '__main__':
    test()
