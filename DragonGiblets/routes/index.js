var express = require('express');
var request = require('request');
var router = express.Router();
var cheerio = require('cheerio');

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
router.post('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});
router.get('/realtime/:symbol', function(req, res, next) {
  var stocks = {};
  request(`http://www.nasdaq.com/symbol/${req.params.symbol}/real-time`, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      var dats = cheerio.load(body);
      stocks = dats('#qwidget_lastsale').text();
      console.log(stocks);
      res.render(`companies/${req.params.symbol}`, { title: 'Realtime Update', stock: stocks });
    }
    else {
      res.end();
    }
  })
});

router.get('/predict', function(req, res, next) {
  // let simcard = {}, symbols = [
  //   'AAPL', 'GOOGL', 'FB', 'AMZN', 'MSFT', 'PMC',
  //   'RARE', 'TREE', 'ALNY', 'ANIP', 'KITE'
  // ];
  //
  // let something = symbols.reduce(function(result, symbol){
  //   request(`http://dev.markitondemand.com/MODApis/Api/v2/Quote?symbol=${symbol}`, function (error, response, body) {
  //     if (!error && response.statusCode == 200) {
  //       var dats = cheerio.load(body);
  //       // Print the body of response.
  //       console.log(result);
  //       result.push({
  //         symbol: dats('symbol').text(),
  //         open: dats('open').text(),
  //         volume: dats('volume').text(),
  //         high: dats('high').text(),
  //         low: dats('low').text()
  //       })
  //     }
  //   })
  //   return result;
  // },[]);
  console.log(something);
  res.render('predict', { title: 'Predict', stock: result });
});


router.get('/aapl', function(req, res, next) {
  res.render('companies/aapl', { title: 'Apple' });
});
router.get('/googl', function(req, res, next) {
  res.render('companies/googl', { title: 'Google' });
});
router.get('/fb', function(req, res, next) {
  res.render('companies/fb', { title: 'Facebook' });
});
router.get('/msft', function(req, res, next) {
  res.render('companies/msft', { title: 'Microsoft' });
});

module.exports = router;
