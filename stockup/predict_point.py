import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from requests import get
from sklearn.ensemble import RandomForestRegressor
import cPickle as pickle
from datetime import date
today = date.today();

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

def predict_point(models, symbol):
    X = process_point(symbol)
    # X = proc_point(dpoint)
    return models[symbol].predict(X)

if __name__=='__main__':
    with open('models.pkl') as f:
        models = pickle.load(f)

    print "Predictions for ", today, "closing price, based on data from 01-01-2011 to ", today
    print predict_point(models, 'AAPL'), 'AAPL'
    print predict_point(models, 'GOOGL'), 'GOOGL'
    print predict_point(models, 'PMC'), 'PMC'
    print predict_point(models, 'MSFT'), 'MSFT'
    print predict_point(models, 'FB'), 'FB'
    print predict_point(models, 'AMZN'), 'AMZN'
    print predict_point(models, 'RARE'), 'RARE'
    print predict_point(models, 'TREE'), 'TREE'
    print predict_point(models, 'ALNY'), 'ALNY'
    print predict_point(models, 'ANIP'), 'ANIP'
    print predict_point(models, 'KITE'), 'KITE'
    # print "Predictions for 07-7-2016 closing price, based on data from 01-01-2011 to 07-06-2016"
    # print predict_point(models, 'AAPL'), 'AAPL'
    # print predict_point(models, 'GOOGL'), 'GOOGL'
    # print predict_point(models, 'PMC'), 'PMC'
    # print predict_point(models, 'MSFT'), 'MSFT'
    # print predict_point(models, 'FB'), 'FB'
    # print predict_point(models, 'AMZN'), 'AMZN'
    # print predict_point(models, 'RARE'), 'RARE'
    # print predict_point(models, 'TREE'), 'TREE'
    # print predict_point(models, 'ALNY'), 'ALNY'
    # print predict_point(models, 'ANIP'), 'ANIP'
    # print predict_point(models, 'KITE'), 'KITE'
    # print predict_point(models, 'GOOGL', [2016-05-23,719.97998,723.5,716.940002,717.25,1233400,'GOOGL',736107]), 'GOOGL 717.25'
    # print predict_point(models, 'PMC', [2016-05-23,26.75,26.76,26.030001,26.16,361900,'PMC',736107]), 'PMC 26.16'
    # print predict_point(models, 'MSFT', [2016-05-23,50.599998,50.68,49.98,50.029999,25999700,'MSFT',736107]), 'MSFT 50.029999'
    # print predict_point(models, 'FB', [2016-05-23,117.419998,117.599998,115.940002,115.970001,20367400,'FB',736107]), 'FB 115.970001'
    # print predict_point(models, 'AMZN', [2016-05-23,704.25,706.0,696.419983,696.75,2579200,'AMZN',736107]), 'AMZN 696.75'
    # print predict_point(models, 'RARE', [2016-05-23,64.089996,67.089996,63.700001,65.190002,417500,'RARE',736107]), 'RARE vol 65.190002'
    # print predict_point(models, 'TREE', [2016-05-23,70.199997,77.519997,69.400002,74.620003,892700,'TREE',736107]), 'TREE vol 74.620003'
    # print predict_point(models, 'ALNY', [2016-05-23,55.119999,56.900002,54.529999,56.07,612300,'ALNY',736107]), 'ALNY vol 56.07'
    # print predict_point(models, 'ANIP', [2016-05-23,49.709999,50.900002,49.040001,49.200001,181400,'ANIP',736107]), 'ANIP vol 49.200001'
    # print predict_point(models, 'KITE', [2016-05-23,47.029999,48.908001,46.689999,48.18,415400,'KITE',736107]), 'KITE vol 48.18'
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
