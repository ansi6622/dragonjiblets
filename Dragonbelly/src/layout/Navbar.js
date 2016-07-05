import React from 'react'
import { Link } from 'react-router'

import NavLink from './../components/NavLink'

const Navbar = (props) => {
  return (
      <nav>
        <NavLink to="/">
          <span>Demo</span>
        </NavLink>
        <i> | </i>
        <NavLink to="/about">
          <span>About</span>
        </NavLink>
      </nav>
  )
};

export default Navbar
