import MainPage from './MainPage';
import Nav from './Nav';
import HatList from './HatList';
import HatForm from './HatForm';
import ShoeList from './ShoeList';
import ShoeForm from './ShoeForm';
import {
  BrowserRouter,
  Routes,
  Route
} from 'react-router-dom';

function App(props) {
  if (props.shoes === undefined && props.hats === undefined) {
    return null;
  }
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
            <Route path="hats">
            <Route index element={<HatList hats={props.hats} />} />
            <Route path="new" element={<HatForm />} />
          </Route>
          <Route path="shoes" element={<ShoeList shoes={props.shoes} />} />
          <Route path="shoes/new" element={<ShoeForm />} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
