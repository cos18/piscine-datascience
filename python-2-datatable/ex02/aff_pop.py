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
        data = load(convert_to_abs("../data/population_total.csv")).T
        data.columns = data.loc['country']
        data = data.iloc[1:].applymap(unit_string_to_raw_string).astype(int)
        data.index = data.index.astype(int)

        _, ax = plt.subplots()
        ax.set(xlabel='Year', ylabel='Population',
               title='Population Projections')
        ax.grid()
        ax.legend()
        data.loc[data.index <= 2050, ['South Korea', 'Japan']].plot()
        plt.show()

        # TODO: 라벨 타이틀 왜안나오지 legend 위치 변경해야함, y축 단위 변경 필요할까?
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()

