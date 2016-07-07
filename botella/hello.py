from bs4 import BeautifulSoup
from requests import get
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
from datetime import date
from bottle import route, run
import requests
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestRegressor
import cPickle as pickle

iris = load_iris()
test_idx = [0,50,100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
clf = tree.DecisionTreeClassifier()
treed = clf.fit(train_data, train_target)
oh = treed.predict(test_data)

# from sklearn.externals.six import StringIO
# import pydot
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file=dot_data)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# graph.write_pdf("iris.pdf")
# #
# from IPython.display import Image
# dot_data = StringIO()
# tree.export_graphviz(clf, out_file=dot_data,
#                          feature_names=iris.feature_names,
#                          class_names=iris.target_names,
#                          filled=True, rounded=True,
#                          special_characters=True)
# graph = pydot.graph_from_dot_data(dot_data.getvalue())
# Image(graph.create_png())
@route('/')
def index():
    # print iris.feature_names, iris.target_names, iris.data[0]
    # print "space"
    print test_target, "trgt"
    print oh, "oh"
    # print test_data, "datas"
    # print clf2.predict(test_data), "peredictionoas"
    return "mew"
@route('/makeprediction')
def index():

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
# numpy type UNSUPPORTED????????//////////////////////////////////////////////////////////////////////////////
        return np.asscalar(predict_point(models, 'AAPL'));
        print "Predictions for 07-6-2016 closing price, based on data from 01-01-2011 to 07-05-2016"
        print predict_point(models, 'GOOGL'), 'GOOGL'
        # print predict_point(models, 'PMC'), 'PMC'
        # print predict_point(models, 'MSFT'), 'MSFT'
        # print predict_point(models, 'FB'), 'FB'
        # print predict_point(models, 'AMZN'), 'AMZN'
        # print predict_point(models, 'RARE'), 'RARE'
        # print predict_point(models, 'TREE'), 'TREE'
        # print predict_point(models, 'ALNY'), 'ALNY'
        # print predict_point(models, 'ANIP'), 'ANIP'
        # print predict_point(models, 'KITE'), 'KITE'
@route('/trainmodel')
def catchall():
    if __name__=='__main__':
        df = pd.read_csv('stock_data.csv')
        models = {}
        for symbol in df["symbol"].unique():
            # pandas trimming and labeling things, date was in format models couldnt read.
            X = df.loc[df['symbol'] == symbol].drop(['symbol', 'close', "date"], axis=1).values
            y = df.loc[df['symbol'] == symbol, "close"].values
            model = RandomForestRegressor(n_estimators=500)
            model.fit(X, y)
            models[symbol] = model
        with open('models.pkl', 'w') as f:
            pickle.dump(models, f)

@route('/getdata')
def doit():
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

@route('/stocks')
def fun():
    # def fut(other):
    #     print other
    #     return requests.get("https://ws.cdyne.com/delayedstockquote/delayedstockquote.asmx/GetQuoteDataSet?StockSymbols=    AAPL&LicenseKey=0")
    # return fut(requests.get("https://ws.cdyne.com/delayedstockquote/delayedstockquote.asmx/GetQuoteDataSet?StockSymbols=AAPL,ALL,AVAV,YPRO,ADBE,ACAD,ACHC,PMC&LicenseKey=0"))
#
# clfMain = tree.DecisionTreeClassifier()
# bumpy = 0
# smooth = 1
# apple = 0
# orange = 1
# features = [[140, smooth], [130, smooth], [150,bumpy], [170, bumpy]]
# labels = [apple,apple,orange,orange]
# clf1 = clfMain.fit(features, labels)
# a1 = clf1.predict([[162, bumpy]])
# @route('/neural')
# def wowfactor():
#     print bumpy,"bumpy", smooth,"smooth", apple,"apple", orange, "orange", features,"features" ,labels, "labels", clf1, "clf", a1
#     print clf1.predict([[120, smooth]])
#     # data format unsupported in browser? type numpy64 bit or watevea
#     return "wowoooowie"
    return requests.get("https://ws.cdyne.com/delayedstockquote/delayedstockquote.asmx/GetQuoteDataSet?StockSymbols=AAPL,ALL,AVAV,YPRO,ADBE,ACAD,ACHC,PMC&LicenseKey=0")
    #
    # @route('/fibStressTest/<id>')
    # def process(id):
    #     def fib(counter):
    #         print counter
    #         # if n == id: return
    #         if counter == 0: return 0
    #         elif counter == 1: return 1
    #         else: return process(counter-1)+process(counter-2)
    #     return fib(float(id))
    #
run(host='localhost', port=8080, debug=True)
# other backup apis
# http://marketdata.websol.barchart.com/getHistory.json?key=39895bae9a46dbe83e26c04b3b387649&symbol=IBM&type=daily&startDate=20150629000000
# http://marketdata.websol.barchart.com/getQuote.json?key=39895bae9a46dbe83e26c04b3b387649&symbols=ZC*1,IBM,GOOGL,
#http://dev.markitondemand.com/MODApis/Api/v2/Quote?symbol=AAPL

# run(host='localhost', port=8080, debug=True)
# AAPL 94.40 2016-06-29T16:00:00+00:00 0.81 93.97 94.55 93.63 36505398 93.59 +0.87% 89.47 - 132.97 8.98 10.51 Apple Inc. false
#  ALL 68.47 2016-06-29T16:01:00+00:00 0.74 67.99 68.53 67.53 3098270 67.73 +1.09% 54.12 - 69.48 4.10 16.71 Allstate Corporation (The) Comm false
#  AVAV 26.69 2016-06-29T16:00:00+00:00 -1.81 26.70 28.52 26.02 954727 28.50 -6.35% 19.10 - 32.44 0.46 57.65 AeroVironment false
#  YPRO 23.69 2016-06-29T15:59:00+00:00 0.05 23.62 23.71 23.62 11724 23.64 +0.22% 21.80 - 24.00 0 0 AdvisorShares YieldPro ETF false
#  ADBE 94.39 2016-06-29T16:00:00+00:00 1.93 92.91 94.62 92.68 2959881 92.46 +2.09% 71.27 - 100.56 1.77 53.33 Adobe Systems Incorporated false ACAD 32.38 2016-06-29T16:00:00+00:00 0.72 32.04 32.72 31.61 1874827 31.66 +2.27% 16.64 - 51.99 -1.68 0 ACADIA Pharmaceuticals Inc. false ACHC 54.97 2016-06-29T16:00:00+00:00 1.65 53.61 56.00 53.58 1110165 53.32 +3.09% 49.77 - 85.62 1.68 32.68 Acadia Healthcare Company false PMC 24.26 2016-06-29T16:01:00+00:00 1.02 23.58 24.31 23.53 128884 23.24 +4.39% 19.79 - 36.96 0.96 25.27 Pharmerica Corporation Common S false
