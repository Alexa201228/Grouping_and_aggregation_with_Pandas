import pandas as pd


def group_data_by_region_column(filename: str):
    df = pd.read_csv(filename, sep=';', header=1)
    group_by_region = df.groupby(['Region', 'Manager'])
    group_by_region.apply(print)


def group_data_by_two_columns(filename: str):
    df = pd.read_csv(filename, sep=';', header=1)
    group_by_region_and_manager = df.groupby(['Region', 'Manager'])
    group_by_region_and_manager.apply(print)


def count_sales_by_manager(filename: str):
    df = pd.read_csv(filename, sep=';', header=1)
    sales_by_manager = df.groupby(['Region', 'Manager']).count()
    sorted_sales = sales_by_manager.sort_values(['Manager'])
    sales_by_manager.apply(print)
    sorted_sales.apply(print)


def least_sales_count(filename: str):
    df = pd.read_csv(filename, sep=';', header=1)
    sales_by_manager = df.groupby(['Region', 'Manager'])['Manager'].count()\
                                                                   .reset_index(name='Count')\
                                                                   .sort_values(['Count'], ascending=True)\
                                                                   .groupby('Region')\
                                                                   .first()
    sales_by_manager.apply(print)


def highest_sales_count(filename: str):
    df = pd.read_csv(filename, sep=';', header=1)
    sales_by_manager = df.groupby(['Region', 'Manager'])['Manager'].count()\
                                                                   .reset_index(name='Count')\
                                                                   .sort_values(['Count'], ascending=True)\
                                                                   .groupby('Region')\
                                                                   .last()
    sales_by_manager.apply(print)


def min_sales_count(filename: str):
    df = pd.read_csv(filename, sep=';', header=1)
    sales_by_manager = df.groupby(['Region', 'Manager'])['Manager'].count().groupby('Region').min()
    print(sales_by_manager)


def max_sales_count(filename: str):
    df = pd.read_csv(filename, sep=';', header=1)
    sales_by_manager = df.groupby(['Region', 'Manager'])['Manager'].count().groupby('Region').max()
    print(sales_by_manager)


def mean_and_median_sales_for_each_manager(filename: str):
    df = pd.read_csv(filename, sep=';', header=1).drop('OrderDate', axis=1)
    median_sales = df.groupby(['Manager']).median()
    mean_sales = df.groupby(['Manager']).mean()
    print(median_sales, mean_sales, sep='\n\n')


def standart_deviation_and_dispersion(filename: str):
    df = pd.read_csv(filename, sep=';', header=1).drop('OrderDate', axis=1)
    deviation = df.groupby(['Region', 'Manager']).std()
    dispersion = df.groupby(['Region', 'Manager']).var()
    print(deviation)
    print(dispersion)


def absolut_standart_deviation(filename: str):
    df = pd.read_csv(filename, sep=';', header=1).drop('OrderDate', axis=1)
    absolute_deviation = df.groupby(['Region', 'Manager']).mad()
    print(absolute_deviation)


def cumulative_volume_and_profit(filename: str):
    df = pd.read_csv(filename, sep=';', header=1).drop(['OrderDate', 'Unit_price'], axis=1)
    volume_and_profit = df.groupby(['Region', 'Manager']).sum()
    print(volume_and_profit)


if __name__ == '__main__':
    min_sales_count('SaleData.csv')
    max_sales_count('SaleData.csv')
