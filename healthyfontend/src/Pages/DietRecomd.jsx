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
          
          <div className="dietrecomd-form">
            <form action="Post">

            <label>Age
              <input className='agebox' type="number" placeholder='Enter Your Age'  />
            </label>
            <label>Gender
              <select>
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
              </select>
            </label>
            <label>Weight
              <input type="number" placeholder='Enter Your Weight' />
            </label>
            <label>Height
              <input type="number" placeholder='Enter Your Heigth' />
            </label>
            <label>Physical activity
              <select>
                <option value="Sedentary">Sedentary</option>
                <option value="Lightlyactive">Lightly active</option>
                <option value="Moderatelyactive ">Moderately active</option>
                <option value="Moderatelyactive "> Extremely active</option>
              </select>
            </label>
            <label>Goal
              <select>
                <option value="Weightloss">Weight Loss </option>
                <option value="Weightgain">Weight Gain</option>
                <option value="MaintainWeight">Maintain Weight</option>
              </select>
            </label>
            <button>Submit</button>
          </form>
          </div>
       </div>
      </div>


  </>
  )
}

export default DietRecomd