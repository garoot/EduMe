import React from 'react';
import './App.css';
import Footer from './components/Footer';
import Navbar from './components/Navbar';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import {GetBlogs, GetBlogDetail} from './components/Blog';
import Sticky from 'react-stickynode';
import MetaTags from 'react-meta-tags';
import NewsLetter from './components/NewsLetter';


function App() {
  return (
    <div class="site-wrapper">
      <head>
        <MetaTags>
          <title>Homepage</title>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        </MetaTags>
        <link href="http://fonts.googleapis.com/css?family=Cabin:400,500,600,bold" rel="stylesheet" type="text/css" />

        <link href="http://fonts.googleapis.com/css?family=PT+Sans+Narrow:regular,bold" rel="stylesheet" type="text/css"/>
      </head>
      <Router>
        <Sticky className="navbar-container" top={0} bottomBoundary={260}>
          <Navbar/>
        </Sticky>

      <div className="content-wrap">
        <Route exact path='/'>
          <GetBlogs />
        </Route>
        <Route path='/blog/:blogId' component={GetBlogDetail} />
      </div>
      <div>
        {/* <NewsLetter/> */}
      </div>
 

        <Footer />
      </Router>
      

    </div>
  );
}

export default App;
