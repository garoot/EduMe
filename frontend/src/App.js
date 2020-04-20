import React from 'react';
import './App.css';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import {GetBlogs, GetBlogDetail} from './components/Blog';



function App() {
  return (
    <div class="site-wrapper">
      <Router>
        <Navbar sticky="top" />

        <Route path='/blogs'>
          <GetBlogs />
        </Route>
        <Route path='/blog/:blogId' component={GetBlogDetail}/>

        <Footer />
      </Router>
      

    </div>
  );
}

export default App;
