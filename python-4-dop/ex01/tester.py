from in_out import outer, square, pow


def test():
    """Test function
    """
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print('---')
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())


if __name__ == '__main__':
    test()
