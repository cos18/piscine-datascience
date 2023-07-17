import matplotlib.pyplot as plt
from load_csv import load, convert_to_abs
from pandas.core.frame import DataFrame
import pandas as pd


def unit_string_to_raw_string(value: str) -> str:
    """Change unit format string to number string

    Args:
        value(str): target string

    Raises:
        TypeError: value string is not unit number

    Returns: number value

    """
    if not isinstance(value, str):
        return value
    unit_dict = {'k': 1000, 'M': 1000000, 'B': 1000000000}
    result = 1
    unit = value[-1]
    if unit not in unit_dict:
        return value
    value = value[:-1]
    result = unit_dict[unit]
    try:
        result *= float(value)
    except ValueError:
        raise TypeError('value string is not unit number')
    return str(int(result))


def get_number_df(dir: str) -> DataFrame:
    """Convert csv raw dataframe to useable DataFrame structure

    Args:
        dir (str): directory to read csv

    Returns:
        DataFrame: Reformatted DataFrame
    """
    data = load(convert_to_abs(dir))
    data.loc[:, '1800':'2050'] = data.loc[:, '1800':'2050'].applymap(
        unit_string_to_raw_string
        ).astype(float)
    return data


def main():
    """
    displays the projection of life expectancy in relation to
    the gross national product ofthe year 1900 for each country
    """
    try:
        income_data = get_number_df(
            '../data/income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        )
        life_data = get_number_df('../data/life_expectancy_years.csv')
        income_data = income_data.rename(columns={'1900': '1900_income'})
        life_data = life_data.rename(columns={'1900': '1900_life'})
        merge_data = pd.merge(
            income_data[['country', '1900_income']],
            life_data[['country', '1900_life']],
            how='inner',
            on='country'
        )

        ax = merge_data.plot.scatter(x='1900_income', y='1900_life')
        ax.set_xscale('log')
        ax.set_xticks([300, 1000, 10000])
        ax.set_xticklabels([300, '1k', '10k'])
        ax.set_yticks([20, 25, 30, 35, 40, 45, 50, 55])
        ax.set_xlabel('Gross domestic product')
        ax.set_ylabel('Life Expectancy')
        ax.set_title('1900')
        plt.show()
    except Exception as err:
        print(f"{type(err).__name__} : {err}")


if __name__ == "__main__":
    main()
