import React from 'react'
import './Services.css'
import foodrecomdimage from '../../assets/food-recommednation.webp'
import foodrecipeimage from '../../assets/recipe.webp'
import foodclasimage from '../../assets/foodimageidentify.webp'
const Services = () => {
  return (

    <>
        <div className='service-container'>
       <h1>Our Services</h1>
       <div className="card-container">
       <div className="card">
       <img src={foodrecomdimage} alt="" />
       <h2>Food recommendation</h2>
       <p>"Get personalized, healthy meal recommendations for your day, making it easy to enjoy delicious and nutritious meals with our fuss-free service."</p>
       <button>Click Here</button>
       </div>
       <div className="card">
       <img src={foodrecipeimage} alt="" />
       <h2>Food Recipe Generator</h2>
       <p>"Explore tailored, nutritious recipes for your day with our recipe generator, making it effortless to savor delicious and healthy meals."</p>
       <button>Click Here</button>
       
       </div>
       <div className="card">
       <img src={foodclasimage} alt="" />
       <h2 id='foodimage'>Food Classification</h2>
       <p>"Explore precise food identification with our advanced image classification technology."</p>
       <button style={{marginTop:'41px'}} className='foodimagebutton'>Click Here</button>
        
        
        
       </div>    
       </div>

       

    </div>
    </>

  )
}

export default Services