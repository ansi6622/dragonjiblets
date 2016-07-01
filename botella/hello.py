from bottle import route, run
import requests

@route('/')
def index():
    return "you started a page"

@route('/hello')
def fun():
    return requests.get("https://ws.cdyne.com/delayedstockquote/delayedstockquote.asmx/GetQuoteDataSet?StockSymbols=AAPL,ALL,AVAV,YPRO,ADBE,ACAD,ACHC,PMC&LicenseKey=0")
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
