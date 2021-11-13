import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Planograms from './RPlanogram';
import reportWebVitals from './reportWebVitals';
import App from './mydata';
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";
ReactDOM.render((
  <BrowserRouter>
  <Routes>
    <Route path="/" element={<Planograms />} />
    <Route exact path="/mydata" element={<App />} />
  </Routes>
</BrowserRouter>),
  document.getElementById('root')
);

reportWebVitals();
