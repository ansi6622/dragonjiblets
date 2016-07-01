const BowerWebpackPlugin = require("bower-webpack-plugin");
const webpack = require('webpack');
const DEV = process.env.NODE_ENV==='development';

const config = {
  entry: './src',
  output: {
    path: './public',
    filename: 'bundle.js'
  },
  devServer:{
    contentBase: 'public',
    historyApiFallback: {
      index: '/index.html'
    }
  },
  devtool: DEV ? 'source-map' : null,
  plugins: [
    new webpack.optimize.OccurenceOrderPlugin(),
    new webpack.EnvironmentPlugin(["NODE_ENV"]),
    new webpack.NoErrorsPlugin()
  ],
  module: {
    loaders: [
      {
        test: /\.js/,
        exclude: /node_modules/,
        loader: 'babel',
        query: {
          presets: ['es2015', 'react', 'stage-1']
        }
      },
      {
        test: /\.scss/,
        exclude: /node_modules/,
        loaders: ['style-loader', 'css-loader', 'sass-loader']
      },
      {
        test: /\.css?$/,
        loader: "style!css!"
      },
      {test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=application/font-woff'},
      {test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=application/octet-stream'},
      {test: /\.eot(\?v=\d+\.\d+\.\d+)?$/, loader: 'file'},
      {test: /\.svg(\?v=\d+\.\d+\.\d+)?$/, loader: 'url?limit=10000&mimetype=image/svg+xml'}
    ]
  },
  plugins: [
        new BowerWebpackPlugin(),
        new webpack.ProvidePlugin({
            $: 'jquery'
        })
    ]
}

if(!DEV){
  config.plugins.push(
    new webpack.optimize.UglifyJsPlugin({
      minimize: true,
      mangle: false,
      compressor: {
        drop_console: true,
        warnings: true
      }
    })
  );
} else {
  config.module.loaders[0].query.presets.push('react-hmre')
}

module.exports = config;


//
// const DEV = process.env.NODE_ENV==='development'
//
// module.exports = {
//   entry: './src/app.js',
//   output: {
//       path: `${__dirname}/public`, //es6 declaration via the back ticks
//       filename: 'bundle.js'
//     },
//
//     devtool: DEV ? 'source-map' : null,
//
//     devServer: {
//       contentBase: 'public',
//       historyApiFallback: {
//         index: '/index.html'
//       }
//     },
//
//     module: {
//       loaders: [
//         {
//           test:/\.js/,
//           loader: 'babel',
//           exclude: /node_modules/,
//           query: {
//             presets: ['es2015', 'react']
//           }
//         },
//         {
//         test:/\.s?css/,
//         loaders: ['style', 'css', 'sass'],
//         exclude: /node_modules/
//       }
//       ]
//     }
// };
