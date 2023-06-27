import sys


def get_morse(c: str) -> str:
    """Convert character to morse string

    Args:
        c (str): character which you want to convert

    Raises:
        AssertionError: If c isn't character or cannot convert to morse

    Returns:
        str: Corresponding Morse Code
    """
    
    NESTED_MORSE = {
        ' ': '/ ',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----'
    }
    c = c.upper()
    if len(c) > 1 or c not in NESTED_MORSE:
        raise AssertionError('the arguments are bad')
    return NESTED_MORSE[c]


def main():
    """
    Make a program that takes a string as an argument
    and encodes it into Morse Code.
    """
    try:
        # Input Error Handling
        argv = sys.argv
        if len(argv) != 2:
            raise AssertionError('the arguments are bad')
        print(' '.join([get_morse(c) for c in argv[1]]))
    except AssertionError as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
