import React, { useState } from 'react'
import logo from '../../assets/logo.png'
import './NavBar.css'
import { Link } from 'react-router-dom'
const NavBar = () => {

  const [menu, setMenu] = useState("Home")
  return (
    <>
      <div className="navbar">
        <div className="nav-log">
          <img src={logo} alt="" />
        </div>
        <ul className="nav-menu">

          <li onClick={() => { setMenu("Home") }}> <Link style={{ textDecoration: 'none', color: 'black' }} to='/'>Home</Link> {menu === "Home" ? <hr /> : <></>}</li>
          <li onClick={() => { setMenu("About Us") }}><Link style={{ textDecoration: 'none', color: 'black' }} to='/aboutus'>About Us</Link>{menu === "About Us" ? <hr /> : <></>} </li>
          <li onClick={() => { setMenu("Services") }}><Link style={{ textDecoration: 'none', color: 'black' }} to='/services'>Services</Link> {menu === "Services" ? <hr /> : <></>} </li>
          <li onClick={() => { setMenu("Contact Us") }}><Link style={{ textDecoration: 'none', color: 'black' }} to='/services'>Contact Us</Link> {menu === "Contact Us" ? <hr /> : <></>} </li>
          <li></li>
        </ul>
        <div className="nav-login">
          <Link to='/login'><button>Login</button></Link>
        </div>
      </div>
    </>

  )
}

export default NavBar