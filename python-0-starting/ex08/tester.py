from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    """
    Main function of tester
    """

    range_len = 5
    sleep_sec = 2
    for elem in ft_tqdm(range(range_len)):
        sleep(sleep_sec)
    print()
    for elem in tqdm(range(range_len)):
        sleep(sleep_sec)
    print()


if __name__ == "__main__":
    main()
