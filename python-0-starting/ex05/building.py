import sys


'''
python building.py "Python 3.0, released in 2008, was a major revision \
that is not completely backward-compatible with earlier versions. \
Python 2 was discontinued with version 2.7.18 in 2020."
'''


def get_standard_input() -> str:
    """Getting Standard input until EOF

    Returns:
        str: string that came from STDIN
    """
    print('What is the text to count?')
    result = ''
    try:
        while True:
            result += input()
            result += '\n'
    except EOFError:
        pass
    return result


def analize_string(value: str) -> dict:
    """Count each character and categorize

    Args:
        value (str): String to analize

    Returns:
        dict: dictionary that contain character category and counts
    """
    result = {
        'upper letters': 0,
        'lower letters': 0,
        'punctuation marks': 0,
        'spaces': 0,
        'digits': 0
    }

    # Defined in https://docs.python.org/ko/3/library/string.html
    for c in value:
        if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result['upper letters'] += 1
        if c in 'abcdefghijklmnopqrstuvwxyz':
            result['lower letters'] += 1
        if c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
            result['punctuation marks'] += 1
        if c in '\t\n\x0b\x0c\r ':
            result['spaces'] += 1
        if c in '0123456789':
            result['digits'] += 1

    return result


def main():
    """
    takes a single string argument and displays the sums of its
    upper-case characters, lower-case characters, punctuation characters,
    digits and spaces.
    """
    try:
        # Setting inputs
        argv = sys.argv
        if len(argv) > 2:
            raise AssertionError('more than one argument is provided')
        value = get_standard_input() if len(argv) != 2 else argv[1]

        # Calculate and print string result
        print(f'The text contains {len(value)} characters:')
        for char_type, cnt in analize_string(value).items():
            print(str(cnt) + ' ' + char_type)
    except AssertionError as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
