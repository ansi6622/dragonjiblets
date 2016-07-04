import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from pymongo import MongoClient
from sklearn.ensemble import RandomForestRegressor
# decisiontree,


def process_stock_df(df, ticker):
    df.drop('Adj Close', axis=1, inplace=True)
    df.columns = df.columns.map(lambda x: x.lower())
    df['symbol'] = ticker
    df['ordinal_date'] = df['date'].dt.to_pydatetime()
    df['ordinal_date'] = df['ordinal_date'].apply(lambda x: x.toordinal())
    return df


def download_data(ticker_lst):
    df_lst = []
    for ticker in ticker_lst:
        url = "http://real-chart.finance.yahoo.com/table.csv?s={0}&a=00&b=12&c=2000&d=06&e=2&f=2016&g=d&ignore=.csv".format(ticker)
        df_lst.append(process_stock_df(pd.read_csv(url, parse_dates=['Date']), ticker))
    df = pd.concat(df_lst, ignore_index=True)
    df = df.sort_values(by='date').reset_index(drop=True)
    return df


if __name__=='__main__':
    # # Create MongoClient
    # client = MongoClient()
    # # Initialize the Database
    # db = client['stock_project']
    # # Connect to the table
    # tab = db['stock_data']
    #
    # point = '''<Quotes diffgr:id="Quotes1" msdata:rowOrder="0" diffgr:hasChanges="inserted">
    # <StockSymbol>AAPL</StockSymbol>
    # <LastTradeAmount>95.89</LastTradeAmount>
    # <LastTradeDateTime>2016-07-01T16:00:00+00:00</LastTradeDateTime>
    # <StockChange>0.29</StockChange>
    # <OpenAmount>95.50</OpenAmount>
    # <DayHigh>96.46</DayHigh>
    # <DayLow>95.33</DayLow>
    # <StockVolume>26026540</StockVolume>
    # <PrevCls>95.60</PrevCls>
    # <ChangePercent>+0.30%</ChangePercent>
    # <FiftyTwoWeekRange>89.47 - 132.97</FiftyTwoWeekRange>
    # <EarnPerShare>8.98</EarnPerShare>
    # <PE>10.67</PE>
    # <CompanyName>Apple Inc.</CompanyName>
    # <QuoteError>false</QuoteError>
    # </Quotes>
    # </QuoteData>'''
    #
    # process_point(point, tab)
    # http://real-chart.finance.yahoo.com/table.csv?s=AAPL&a=00&b=12&c=2000&d=06&e=2&f=2016&g=d&ignore=.csv

    df = download_data(['AAPL', 'AAL', 'PMC'])

    for symbol in df['symbol'].unique():
        ts = pd.Series(df.loc[df['symbol'] == symbol, 'close'].values, index=df.loc[df['symbol'] == symbol, 'date'])
        ts.plot(label=symbol)
    plt.legend(loc='best')
    plt.show()

    # y = df.pop('close').values
    # X = df.values

    models = {}
    for symbol in df['symbol'].unique():
        X = df.loc[df['symbol'] == symbol].drop(['symbol', 'close', 'date'], axis=1).values
        y = df.loc[df['symbol'] == symbol, 'close'].values

        model = RandomForestRegressor(n_estimators=500)
        model.fit(X, y)

        models[symbol] = model
