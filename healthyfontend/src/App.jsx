import './App.css'
import NavBar from './Components/NavBar/NavBar'
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Home from './Pages/Home'
import DietRecomd from './Pages/DietRecomd'
import FoodImage from './Pages/FoodImage'
import Recipe from './Pages/Recipe'
import AboutUs from './Pages/AboutUs'
import Services from './Pages/Services'
import ContactUs from './Pages/ContactUs'
function App() {

  return (
    <>
    <BrowserRouter>
    <NavBar/>
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/aboutus' element={<AboutUs/>}/>
      <Route path='/service' element={<Services/>}/>
      <Route path='/contact' element={<ContactUs/>}/>
      
    </Routes>
        
    </BrowserRouter>
    </>
  )
}

export default App
