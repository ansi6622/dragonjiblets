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

def proc_point(dpoint):
    return np.array([dpoint[1],dpoint[2],dpoint[3],dpoint[5],dpoint[7]]).reshape(1, -1)

def predict_point(models, symbol, dpoint):
    # X = process_point(symbol)
    X = proc_point(dpoint)
    return models[symbol].predict(X)


if __name__=='__main__':
    with open('models.pkl') as f:
        models = pickle.load(f)

    print "Predictions for 06-07-2016 closing price, based on data from 01-01-2011 to 06-06-2016"
    print predict_point(models, 'AAPL', [2016-06-07,99.25,99.870003,98.959999,99.029999,22366400,'AAPL',736122]), 'AAPL 99.029999'
    print predict_point(models, 'GOOGL', [2016-06-07,733.27002,736.710022,730.799988,731.090027,1214700,'GOOGL',736122]), 'GOOGL 731.090027'
    print predict_point(models, 'PMC', [2016-06-07,26.200001,26.639999,25.870001,26.35,218800,'PMC',736122]), 'PMC 26.35'
    print predict_point(models, 'MSFT', [2016-06-07,52.240002,52.73,52.099998,52.099998,20794000,'MSFT',736122]), 'MSFT 52.099998'
    print predict_point(models, 'FB', [2016-06-07,119.239998,119.300003,117.669998,117.760002,17053700,'FB',736122]), 'FB 117.760002'
    print predict_point(models, 'AMZN', [2016-06-07,729.890015,730.0,720.549988,723.73999,2719700,'AMZN',736122]), 'AMZN 723.73999'
    print predict_point(models, 'RARE', [2016-06-07,71.669998,71.855003,68.620003,70.169998,678400,'RARE',736122]), 'RARE vol 70.169998'
    print predict_point(models, 'TREE', [2016-06-07,88.269997,90.269997,87.800003,89.510002,471500,'TREE',736122]), 'TREE vol 89.510002'
    print predict_point(models, 'ALNY', [2016-06-07,71.400002,72.639999,69.68,71.050003,845100,'ALNY',736122]), 'ALNY vol 71.050003'
    print predict_point(models, 'ANIP', [2016-06-07,55.25,56.400002,54.5,55.52,138800,'ANIP',736122]), 'ANIP vol 55.52'
    print predict_point(models, 'KITE', [2016-06-07,57.41,57.91,55.450001,56.060001,881200,'KITE',736122]), 'KITE vol 56.060001'



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
