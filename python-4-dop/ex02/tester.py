from callLimit import callLimit


def test():
    """Test function
    """
    @callLimit(3)
    def f():
        """Test f function
        """
        print('f()')

    @callLimit(1)
    def g():
        """Test g function
        """
        print('g()')

    for i in range(3):
        f()
        g()


if __name__ == '__main__':
    test()
