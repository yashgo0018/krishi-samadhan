import './App.css';
// import Navbar from './components/navbar';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom';
import Disease from './components/disease';
import Navbar from './components/navbar';
import Home from './components/home';
import Predictsoil from './components/predictsoil';
import Footer from './components/footer';
import RegisterUser from './components/registerUser';
import HelpingHand from './components/helpingHand';
import Ngo from './components/ngo';

function App() {
  return (
    <Router>
      <Navbar/>
      <Routes>
      <Route exact path='/' element={<Home/>}/>
      <Route exact path='/disease' element={<Disease/>} />
      <Route exact path='/predsoil' element={<Predictsoil />} />
      <Route exact path='/registerUser' element={<RegisterUser />} />
      <Route exact path='/helpingHand' element={<HelpingHand />} />
      <Route exact path='/store' element={<Ngo/>} />
      </Routes>
      <Footer/>
    </Router>
  );
}
export default App;