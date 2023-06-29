from load_csv import load, convert_to_abs


def main():
    """
    Test function of this exercise
    """

    print(load(convert_to_abs("../data/life_expectancy_years.csv")))
    try:
        load(convert_to_abs("file_not_exist.csv"))
    except FileNotFoundError as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
