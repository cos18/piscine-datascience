import sys
from ft_fliter import ft_filter


def main():
    """
    output a list of words from S that have a length greater than N
    """
    try:
        # Input Error Handling
        argv = sys.argv
        if len(argv) != 3:
            raise AssertionError('the arguments are bad')
        n = 0
        try:
            n = int(argv[2])
        except ValueError:
            raise AssertionError('the arguments are bad')

        print(ft_filter(lambda word: len(word) > n, argv[1].split()))
    except AssertionError as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
