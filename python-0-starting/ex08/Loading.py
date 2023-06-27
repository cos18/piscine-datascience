from time import time
import os


def sec_to_string(sec: int) -> str:
    """Convert Second number to String

    Args:
        sec (int): second value represented to number

    Returns:
        str: time string
            ex) 63   => 01:03
                3599 => 59:59
                3601 => 1:00:01
    """
    format_sec = int(sec % 60)
    sec /= 60
    format_min = int(sec % 60)
    result = "{:02d}:{:02d}".format(format_min, format_sec)
    sec /= 60
    if int(sec) > 0:
        result = str(int(sec)) + ":" + result
    return result


def progress_to_string(progress: float, length: int) -> str:
    """Convert progress float value to loading bar string

    Args:
        progress (float): progress value represented to float
        length (int):
            length of progress bar.
            Minimum is 2 and it will set if value is below to 2

    Returns:
        str: loading bar string
    """
    if length < 2:
        length = 2
    fill_cnt = int(progress * length)
    return '█' * fill_cnt + ' ' * (length - fill_cnt)


def print_status(
    index: int,
    length: int,
    start_time: float
):
    """Print Status Bar

    Args:
        index (int): index of iterator item
        length (int): length of iterator
        start_time (float): second which start the iterator
    """
    terminal_columns, _ = os.get_terminal_size(0)
    spend_time = time() - start_time
    progress = index / length
    percent_str = '{:3d}%|'.format(int(progress * 100))
    number_str = '| {}/{} [{}<{}, '.format(
        index,
        length,
        sec_to_string(int(spend_time)),
        '?' if index == 0 else (
            '00:00' if index == length else sec_to_string(
                int(spend_time * (length - index) / index)
            )
        )
    )
    if index == 0:
        number_str += '?it/s]'
    elif index > spend_time:
        number_str += '{:5.2f}it/s]'.format(index / spend_time)
    else:
        number_str += '{:5.2f}s/it]'.format(spend_time / index)

    result = percent_str
    result += progress_to_string(progress,
                                 terminal_columns
                                 - len(percent_str)
                                 - len(number_str))
    result += number_str
    print(f'\r{result[:terminal_columns]}', end='')


def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """

    lst_len = len(lst)

    if lst_len == 0:
        print('0it [00:00, ?it/s]')
        return

    start_time = time()
    for index, item in enumerate(lst):
        print_status(index, lst_len, start_time)
        yield item
    print_status(lst_len, lst_len, start_time)
