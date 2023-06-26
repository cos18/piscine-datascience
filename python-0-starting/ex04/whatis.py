import sys
try:
    argv = sys.argv
    if len(argv) < 2:
        exit(0)
    if len(argv) != 2:
        raise AssertionError('more than one argument is provided')
    try:
        value = int(argv[1])
        print(f"I'm {'Odd' if value % 2 else 'Even'}.")
    except ValueError:
        raise AssertionError('argument is not an integer')
except AssertionError as err:
    print(f"{type(err).__name__} : {err}")
