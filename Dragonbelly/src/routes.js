import React, { Component } from 'react'
import { Router, Route, IndexRoute, browserHistory, hashHistory } from 'react-router'

import transitionAuth from './helpers/transition_auth'
import Layout from './layout/Layout'
import NotFound from './pages/NotFound'
import Home from './pages/Home'
import HomeIndex from './pages/home/HomeIndex'
import AboutPage from './pages/home/AboutPage'
import QuickStockPage from './pages/home/QuickStock'
import RealtimeQuotePage from './pages/home/realtimeQuote'


const Routes = () =>(
  <Router history={hashHistory}>
    <Route component={Layout}>

      <Route path="/" component={Home}>
        <IndexRoute component={HomeIndex}/>
        <Route path="/about" component={AboutPage}/>
        <Route path="/quick" component={QuickStockPage}/>
        <Route path="/real" component={RealtimeQuotePage}/>
      </Route>

      <Route path="*" component={NotFound} />

    </Route>
  </Router>
);

export default Routes
