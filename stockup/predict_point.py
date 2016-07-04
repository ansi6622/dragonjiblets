import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from requests import get
from sklearn.ensemble import RandomForestRegressor
import cPickle as pickle

# using BeautifulSoup to parse through data, returning a reshaped numpy array for the model
def process_point(symbol):
    xml = get("https://ws.cdyne.com/delayedstockquote/delayedstockquote.asmx/GetQuoteDataSet?StockSymbols={0}&LicenseKey=0".format(symbol))
    soup = BeautifulSoup(xml.content, 'xml')
    open_amount = float(soup.find('OpenAmount').text)
    high_amount = float(soup.find('DayHigh').text)
    low_amount = float(soup.find('DayLow').text)
    volume = int(soup.find('StockVolume').text)
    date_ordinal = pd.to_datetime(soup.find('LastTradeDateTime').text).toordinal()
    return np.array([open_amount, high_amount, low_amount, volume, date_ordinal]).reshape(1, -1)


def predict_point(models, symbol):
    X = process_point(symbol)
    return models[symbol].predict(X)


if __name__=='__main__':
    with open('models.pkl') as f:
        models = pickle.load(f)

    print predict_point(models, 'ALNY'), 'alny'
    print predict_point(models, 'ANIP'), 'anip'
    print predict_point(models, 'KITE'), 'kite'

# july 1,
# 'AAPL' [ 95.89815912],
# 'GOOGL' [ 710.43108029],
# 'PMC' [ 24.99928068],
 # 'MSFT' [ 51.15683992],
 # [ 114.38654155] facebook
# [ 725.35809375] amazon
# [ 51.30313932] rare pharm
# [ 92.14649767] tree,
# [ 60.32483923] alny
# [ 57.11150073] anip
# [ 50.75742063] kite