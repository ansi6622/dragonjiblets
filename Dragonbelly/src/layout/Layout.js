import React, { Component } from 'react'

import Navbar from './Navbar'

class Layout extends Component{

  render(){
    return(
      <div>
        <Navbar/>
        <main>
          {this.props.children}
        </main>

      </div>
    )
  }
}

Layout.contextTypes = {
  router: React.PropTypes.object
};

export default Layout
