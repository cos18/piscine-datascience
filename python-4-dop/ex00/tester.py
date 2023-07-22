from statistics import ft_statistics


def test():
    """Test function
    """
    ft_statistics(1, 42, 360, 11, 64, to="mean", tu="median", ta="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, e="heheh", ej="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")
    print("-----")

    ft_statistics(True, False, 1, 2, 3, toto="mean")


if __name__ == '__main__':
    test()
