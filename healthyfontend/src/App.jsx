import './App.css'
import NavBar from './Components/NavBar/NavBar'
import {BrowserRouter,Routes,Route} from 'react-router-dom'
import Home from './Pages/Home'
import DietRecomd from './Pages/DietRecomd'
import FoodImage from './Pages/FoodImage'
import Recipe from './Pages/Recipe'
function App() {

  return (
    <>
    <BrowserRouter>
    <NavBar/>
    <Routes>
      <Route path='/' element={<Home/>}/>
      <Route path='/dietrecommend' element={<DietRecomd/>}/>
      <Route path='/foodimage' element={<FoodImage/>}/>
      <Route path='/recipe' element={<Recipe/>}/>
      
    </Routes>
        
    </BrowserRouter>
    </>
  )
}

export default App
