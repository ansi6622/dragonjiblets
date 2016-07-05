import React from 'react'
import IconLink from '../../components/IconLink'

const HomeIndex = () =>(
  <div className="homeIndex">
    <h1 className="homeIndex">Welcome to Dragon Jiblets</h1>
      <IconLink
      pathTo={"/about"}
      title={"History"}
      color={"rgba(131, 222, 224, 0.74)"}
      icon={"glyphicon glyphicon-volume-up center-block"}
      />
      <IconLink
      pathTo={"/real"}
      title={"Models"}
      color={"rgba(219, 144, 148, 0.84)"}
      icon={"glyphicon glyphicon-list-alt center-block"}
      />
      <IconLink
      pathTo={"/quick"}
      title={"QuickStocks"}
      color={"rgba(240, 186, 141, 0.95)"}
      icon={"glyphicon glyphicon-cog center-block"}
      />

  </div>
);

export default HomeIndex
