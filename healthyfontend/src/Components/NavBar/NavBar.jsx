import React, { useState } from 'react'
import logo from '../../assets/logo.png'
import './NavBar.css'
const NavBar = () => {

  const [menu,setMenu] =  useState("Home")
  return (
    <>
         <div className="navbar">
            <div className="nav-log">
              <img src={logo} alt="" />
            </div>
            <ul className="nav-menu">
               <li onClick={()=>{setMenu("Home")}}>Home {menu==="Home"? <hr />: <></>}</li>
               <li onClick={()=>{setMenu("About Us")}}>About Us {menu==="About Us"? <hr />: <></>} </li>
               <li onClick={()=>{setMenu("Services")}}>Services {menu==="Services"? <hr />: <></>} </li>
               <li onClick={()=>{setMenu("Contact Us")}}>Contact Us {menu==="Contact Us"? <hr />: <></>} </li>
               <li></li>
            </ul>
            <div className="nav-login">
              <button>Login</button>
            </div>
         </div>
    </>

  )
}

export default NavBar