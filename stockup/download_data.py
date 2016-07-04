import pandas as pd
import numpy as np
from datetime import date


def process_stock_df(df, ticker):
    df.drop('Adj Close', axis=1, inplace=True)
    df.columns = df.columns.map(lambda x: x.lower())
    df['symbol'] = ticker
    df['ordinal_date'] = df['date'].dt.to_pydatetime()
    df['ordinal_date'] = df['ordinal_date'].apply(lambda x: x.toordinal())
    return df


def download_data(ticker_lst):
    df_lst = []
    today = date.today()
    for ticker in ticker_lst:
        url = "http://real-chart.finance.yahoo.com/table.csv?s={0}&a=00&b=01&c=2011&d={1}&e={2}&f={3}&g=d&ignore=.csv".format(ticker, today.month-1, today.day-1, today.year)
        df_lst.append(process_stock_df(pd.read_csv(url, parse_dates=['Date']), ticker))
    df = pd.concat(df_lst, ignore_index=True)
    df = df.sort_values(by='date').reset_index(drop=True)
    return df


if __name__=='__main__':
    df = download_data(['AAPL', 'GOOGL', 'PMC', 'MSFT', 'FB', 'AMZN', 'RARE', 'TREE', 'ALNY', 'ANIP', 'KITE'])
    df.to_csv('stock_data.csv', index=False)


# 'AAPL', 'GOOGL', 'PMC', 'MSFT', 'FB', 'AMZN', 'RARE', 'TREE', 'ALNY', 'ANIP', 'KITE'
