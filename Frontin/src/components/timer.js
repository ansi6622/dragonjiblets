import React, { Component } from 'react'
export default class Timer extends Component {
  constructor(){
    super();
    this.state = {
    count: 0
    }
  }
  componentWillMount(){
    let i = 1;
    setInterval(()=>{
      this.setState({
        count: i++
      })
    }, 1000)
  }
  render(){
    if(this.state.count%5 ==  0){
      return <div> <img src="http://images1.miaminewtimes.com/imager/u/745xauto/8203153/feature1-4-8c59f2cd305f744b.jpg" />  </div>
    }
    else {
    return (
      <div>
      {this.state.count}
      </div>
    )
  }
}
}
