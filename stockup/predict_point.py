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

    print "Predictions for 06-20-2016 closing price, based on data from 01-01-2011 to 06-17-2016"
    print predict_point(models, 'AAPL', [2016-06-17,96.620003,96.650002,95.300003,95.330002,60595000,'AAPL',736132]), 'AAPL 95.330002'
    print predict_point(models, 'GOOGL', [2016-06-17,721.390015,721.390015,701.119995,704.25,4111000,'GOOGL',736132]), 'GOOGL 704.25'
    print predict_point(models, 'PMC', [2016-06-17,24.610001,24.879999,24.09,24.190001,317600,'PMC',736132]), 'PMC 24.190001'
    print predict_point(models, 'MSFT', [2016-06-17,50.41,50.43,49.82,50.130001,45670500,'MSFT',736132]), 'MSFT 50.130001'
    print predict_point(models, 'FB', [2016-06-17,114.419998,114.43,112.559998,113.019997,24383100,'FB',736132]), 'FB 113.019997'
    print predict_point(models, 'AMZN', [2016-06-17,718.190002,718.200012,699.179993,706.390015,5824300,'AMZN',736132]), 'AMZN 706.390015'
    print predict_point(models, 'RARE', [2016-06-17,58.740002,58.825001,54.720001,54.990002,1339300,'RARE',736132]), 'RARE vol 54.990002'
    print predict_point(models, 'TREE', [2016-06-17,74.400002,77.080002,71.339996,72.25,656400,'TREE',736132]), 'TREE vol 72.25'
    print predict_point(models, 'ALNY', [2016-06-17,58.299999,58.34,55.810001,55.970001,905100,'ALNY',736132]), 'ALNY vol 55.970001'
    print predict_point(models, 'ANIP', [2016-06-17,56.049999,56.049999,52.52,52.84,505700,'ANIP',736132]), 'ANIP vol 52.84'
    print predict_point(models, 'KITE', [2016-06-17,52.66,53.269001,49.599998,49.73,821800,'KITE',736132]), 'KITE vol 49.73'

2016-06-20,56.279999,57.150002,54.09,54.5,976300,RARE,736135
2016-06-20,50.68,51.470001,50.0,51.09,770000,KITE,736135
2016-06-20,713.5,721.309998,710.809998,714.01001,3668200,AMZN,736135
2016-06-20,113.769997,114.720001,112.75,113.370003,20674700,FB,736135
2016-06-20,710.309998,715.869995,705.409973,706.130005,2269500,GOOGL,736135
2016-06-20,53.810001,54.029999,52.549999,53.09,171700,ANIP,736135
2016-06-20,50.639999,50.830002,50.029999,50.07,35559500,MSFT,736135
2016-06-20,24.290001,25.1,24.26,24.629999,223600,PMC,736135
2016-06-20,96.0,96.57,95.029999,95.099998,33942300,AAPL,736135
2016-06-20,56.98,58.689999,56.41,56.639999,863900,ALNY,736135
2016-06-20,73.93,77.919998,71.82,76.959999,501300,TREE,736135
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
