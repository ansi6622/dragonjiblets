from bottle import route, run
import numpy as np
import requests
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()
test_idx = [0,50,100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
clf = tree.DecisionTreeClassifier()
treed = clf.fit(train_data, train_target)
oh = treed.predict(test_data)

from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")
#
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
#
@route('/stocks')
def fun():
    def fut(other):
        print other
        return requests.get("https://ws.cdyne.com/delayedstockquote/delayedstockquote.asmx/GetQuoteDataSet?StockSymbols=    ADBE,PMC&LicenseKey=0")
    return fut(requests.get("https://ws.cdyne.com/delayedstockquote/delayedstockquote.asmx/GetQuoteDataSet?StockSymbols=AAPL,ALL,AVAV,YPRO,ADBE,ACAD,ACHC,PMC&LicenseKey=0"))
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
