import React from 'react';
import './App.css';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import {GetBlogs, GetBlogDetail} from './components/Blog';
import Sticky from 'react-stickynode';



function App() {
  return (
    <div class="site-wrapper">
      <Router>
        <Sticky className="navbar-container" top='#header' bottomBoundary='#content'>
          <Navbar/>
        </Sticky>
        


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
