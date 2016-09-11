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

def download_data(df, ticker_lst):
    df_lst = []
    today = date.today()
    for ticker in ticker_lst:
        last_date = df.loc[df['symbol'] == ticker, 'date'].max()
        if today.isoweekday > 5:
            today = date(today.year, today.month, today.day - (today.isoweekday()-5))
        url = "http://real-chart.finance.yahoo.com/table.csv?s={0}&a={1}&b={2}&c={3}&d={4}&e={5}&f={6}&g=d&ignore=.csv".format(ticker, last_date.month-1, last_date.day-4, last_date.year, today.month-1, today.day, today.year)
        df_lst.append(process_stock_df(pd.read_csv(url, parse_dates=['Date']), ticker))
    df = pd.concat(df_lst, ignore_index=True)
    df = df.sort_values(by='date').reset_index(drop=True)
    return df

def update_csv(csv_name):
    df_old = pd.read_csv(csv_name, parse_dates=['date'])
    df = download_data(df_old, ['AAPL', 'GOOGL', 'PMC', 'MSFT', 'FB', 'AMZN', 'RARE', 'TREE', 'ALNY', 'ANIP', 'KITE'])
    df.to_csv(csv_name, index=False)
