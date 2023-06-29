from load_csv import load, convert_to_abs


def main():
    """
    loads the file `life_expectancy_years.csv`,
    and displays the South Korea information
    """

    load(convert_to_abs("../data/life_expectancy_years.csv"))


if __name__ == "__main__":
    main()
