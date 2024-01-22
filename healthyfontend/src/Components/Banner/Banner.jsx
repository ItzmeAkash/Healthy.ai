import React, { useState } from 'react'
import './Banner.css'
import banner from '../../assets/banner.png'
import { Link } from 'react-router-dom'

const Banner = () => {

 
  return (
    <div className='banner-container'>
       <div className="banner-text">
           <h1>"Prioritize a healthy lifestyle"</h1>
           <div className="button-container">
         <Link style={{textDecoration:'none'}} to='/service'><button >Service</button></Link> 
        </div>
       </div>
       
       <div className="banner-image">
         <img src={banner} alt="" />
       </div>
    </div>
  )
}

export default Banner