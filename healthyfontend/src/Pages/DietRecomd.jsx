import React from 'react'
import './Css/DietRecomd.css'
import Banner from '../Components/Banner/Banner'

const DietRecomd = (props) => {
  return (
  <>
      <div className='dietrecomd-contrainer'>
         <Banner text={props.text}/>
       
      </div>


  </>
  )
}

export default DietRecomd