import React from 'react';
import './App.css';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import {GetBlogs, GetBlogDetail} from './components/Blog';
import Sticky from 'react-stickynode';
import MetaTags from 'react-meta-tags';


function App() {
  return (
    <div class="site-wrapper">
      <head>
        <MetaTags>
          <title>Hello</title>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        </MetaTags>
      </head>
      <Router>
        <Sticky className="navbar-container" top={0} bottomBoundary={260}>
          <Navbar/>
        </Sticky>

      <div className="content-wrap">
          <Route path='/blogs'>
            <GetBlogs />
          </Route>
          <Route path='/blog/:blogId' component={GetBlogDetail} />
      </div>
 

        <Footer />
      </Router>
      

    </div>
  );
}

export default App;
