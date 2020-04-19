import React from 'react';
import './App.css';
import Blog from './components/Blog';
import Footer from './components/Footer';
import Navbar from './components/Navbar';


function App() {
  return (
    <div class="site-wrapper">
      <Navbar sticky="top" />

      <Blog />
      <Footer />

    </div>
  );
}

export default App;
