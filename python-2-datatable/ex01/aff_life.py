import matplotlib.pyplot as plt
from load_csv import load, convert_to_abs


def unit_string_to_raw_string(value: str) -> str:
    """Change unit format string to number string

    Args:
        value(str): target string

    Raises:
        TypeError: value string is not unit number

    Returns: number value

    """
    unit_dict = {'k': 1000, 'M': 1000000, 'B': 1000000000}
    result = 1
    unit = value[-1]
    if unit in unit_dict:
        value = value[:-1]
        result = unit_dict[unit]
    try:
        result *= float(value)
    except ValueError:
        raise TypeError('value string is not unit number')
    return str(int(result))

def main():
    """
    loads the file `population_total.csv`,
    and displays South Korea versus Japan
    """
    try:
        data = load(convert_to_abs("../data/population_total.csv"))
        data = data.set_index('country').applymap(unit_string_to_raw_string).astype(int)

        _, ax = plt.subplots()
        ax.set(xlabel='Year', ylabel='Population',
               title='Population Projections')
        ax.legend()
        ax.grid()
        data.loc['South Korea'].plot()
        plt.show()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
