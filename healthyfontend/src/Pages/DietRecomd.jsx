import React from 'react'
import './Css/DietRecomd.css'
import Banner from '../Components/Banner/Banner'

const DietRecomd = (props) => {
  return (
  <>
      <div className='dietrecomd-contrainer'>
         <Banner text={props.text}/>
       <div className="dietrecomd">
          <h1>Diet Food Recommendation</h1>
       </div>
      </div>


  </>
  )
}

export default DietRecomd