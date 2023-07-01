import matplotlib.pyplot as plt
from load_csv import load, convert_to_abs


def main():
    """
    loads the file `life_expectancy_years.csv`,
    and displays the South Korea information
    """
    try:
        data = load(convert_to_abs("../data/life_expectancy_years.csv"))
        data = data.set_index('country')
        _, ax = plt.subplots()
        ax.set(xlabel='Year', ylabel='Life expectancy',
               title='South Korea Life Expectancy Projections')
        ax.grid()
        data.loc['South Korea'].plot()
        plt.show()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
