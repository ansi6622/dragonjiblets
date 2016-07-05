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

    print predict_point(models, 'AAPL'), 'AAPL'
    print predict_point(models, 'GOOGL'), 'GOOGL'
    print predict_point(models, 'PMC'), 'PMC'
    print predict_point(models, 'MSFT'), 'MSFT'
    print predict_point(models, 'FB'), 'FB'
    print predict_point(models, 'AMZN'), 'AMZN'
    print predict_point(models, 'RARE'), 'RARE vol'
    print predict_point(models, 'TREE'), 'TREE vol'
    print predict_point(models, 'ALNY'), 'alny vol'
    print predict_point(models, 'ANIP'), 'anip vol'
    print predict_point(models, 'KITE'), 'kite vol'

# july 1,
# 'AAPL' [ 95.89815912],
# 'GOOGL' [ 710.43108029],
# 'PMC' [ 24.99928068],
 # 'MSFT' [ 51.15683992],
 # [ 114.38654155] facebook
# [ 725.35809375] amazon
# [ 51.30313932] rare pharm
# [ 92.14649767] tree,
# [ 60.32483923] alny -.0722 on second predict
# [ 57.11150073] anip +.0477 on second predict
# [ 50.75742063] kite -.0193 on second predict

# 3rd predict
# [ 95.88119931] AAPL
# [ 710.57963995] GOOGL
# [ 24.99594068] PMC
# [ 51.15600003] MSFT
# [ 114.36570161] FB
# [ 725.4281145] AMZN
# [ 51.27661925] RARE vol
# [ 92.12637795] TREE vol
# [ 60.25269929] alny vol
# [ 57.14920077] anip vol
# [ 50.73810055] kite vol
