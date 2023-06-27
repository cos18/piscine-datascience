from ft_package import count_in_list


def main():
    """
    Test function of this exercise
    """
    print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
    print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0


if __name__ == "__main__":
    main()
