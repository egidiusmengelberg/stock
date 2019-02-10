import os
import pandas as pd

import parsing_keystats
import stock_prediction
import current_data


def test_forward_sample_dimensions():
    df = pd.read_csv('forward_sample.csv')
    indexing_columns = ['Date', 'Unix', 'Ticker', 'Price',
                        'stock_p_change', 'SP500', 'SP500_p_change']
    n_cols = len(df.columns)
    assert n_cols == len(current_data.features) + len(indexing_columns)
    assert len(df) == len(os.listdir('forward/'))
    indexing_columns.remove('Ticker')
    assert df[indexing_columns].sum().sum() == 0


def test_forward_sample_data():
    df = pd.read_csv('forward_sample.csv')
    df.fillna(0, inplace=True)

    positive_features = ['Market Cap', 'Price/Sales', 'Revenue', 'Revenue Per Share', 'Total Cash',
                         'Total Cash Per Share', 'Total Debt', '50-Day Moving Average', '200-Day Moving Average',
                         'Avg Vol (3 month)', 'Shares Outstanding', 'Float',
                         '% Held by Insiders', '% Held by Institutions', 'Shares Short',
                         'Short Ratio', 'Short % of Float', 'Shares Short (prior month']
    assert all(df[positive_features] >= 0)

    fractional_features = ['% Held by Insiders', '% Held by Institutions',
                           'Short Ratio', 'Short % of Float']
    assert all(df[fractional_features] <= 100)


def test_stock_prices_dataset():
    df = pd.read_csv("stock_prices.csv", index_col='Date', parse_dates=True)
    assert type(df.index) == pd.core.indexes.datetimes.DatetimeIndex
    assert all(df.isnull().sum() < len(df))
    df.fillna(0, inplace=True)
    assert all(df >= 0)

    index_df = pd.read_csv(
        "sp500_index.csv", index_col='Date', parse_dates=True)
    assert type(df.index) == pd.core.indexes.datetimes.DatetimeIndex
    assert len(index_df.columns) == 6
    assert index_df.shape[0] == df.shape[0]
    assert index_df.isnull().sum().sum() == 0


def def_keystats_dimensions():
    df = pd.read_csv("keystats.csv", index_col='Date')

    indexing_columns = ['Unix', 'Ticker', 'Price',
                        'stock_p_change', 'SP500', 'SP500_p_change']
    n_cols = len(df.columns)
    assert n_cols == len(parsing_keystats.features) + len(indexing_columns)

    assert df[indexing_columns].isnull().sum().sum() == 0


def test_stock_prediction_dataset():
    df = pd.read_csv("keystats.csv", index_col='Date')
    num_rows_with_nan = sum(df.isnull().sum(axis=1) > 0)

    X, y = stock_prediction.build_data_set()
    assert X.shape[0] == df.shape[0] - num_rows_with_nan
    assert len(y) == df.shape[0] - num_rows_with_nan
    assert X.shape[1] == len(parsing_keystats.features)
