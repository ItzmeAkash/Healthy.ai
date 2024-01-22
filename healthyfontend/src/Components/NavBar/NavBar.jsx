import React, { useState } from 'react'
import logo from '../../assets/logo.png'
import './NavBar.css'
import { Link } from 'react-router-dom'
import { FaBars } from "react-icons/fa";
const NavBar = () => {

  const [menu, setMenu] = useState("Home")
  const [isMenuVisible, setMenuVisible] = useState(false);

  const handleMenuToggle = () => {
    setMenuVisible(!isMenuVisible);
  };
  const handleMenuItemClick = (menuItem) => {
    setMenu(menuItem);
    setMenuVisible(false);
  };

  return (
    <>
      <div className="navbar">
        <div className="nav-log">
          <img src={logo} alt="" />
        </div>

        <ul className={`nav-menu ${isMenuVisible ? 'visible' : ''}`}>
          <li onClick={() => handleMenuItemClick('Home')}>
            <Link style={{textDecoration:'none', color:'black'}} to="/">Home</Link>
            {menu === 'Home' ? <hr /> : <></>}
          </li>
          <li onClick={() => handleMenuItemClick('About Us')}>
            <Link style={{textDecoration:'none', color:'black'}} to="/aboutus">About Us</Link>
            {menu === 'About Us' ? <hr /> : <></>}
          </li>
          <li onClick={() => handleMenuItemClick('Services')}>
            <Link style={{textDecoration:'none', color:'black'}} to="/service">Services</Link>
            {menu === 'Services' ? <hr /> : <></>}
          </li>
          <li onClick={() => handleMenuItemClick('Contact Us')}>
            <Link style={{textDecoration:'none', color:'black'}} to="/contactus">Contact Us</Link>
            {menu === 'Contact Us' ? <hr /> : <></>}
          </li>
        </ul>

        <div className="nav-login">
          <Link to="/login">
            <button>Login</button>
          </Link>
        </div>

        <button className="menu-bars" onClick={handleMenuToggle}>
          <FaBars />
        </button>
      </div>
    </>
  );
};

export default NavBar;