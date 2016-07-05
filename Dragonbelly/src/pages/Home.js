import React, { Component } from 'react'
import { connect } from 'react-redux'
import { verifyUser } from '../redux/actions'

class Home extends Component{
  componentWillMount(){
    return false;
  }
  render(){
    return(
      <div>
        {this.props.children}
      </div>
    )
  }
}

Home.contextTypes = {
  router: React.PropTypes.object
};

function mapStateToProps(state) {
  return {user: state}
}

export default connect(mapStateToProps, {
  verifyUser
})(Home);
