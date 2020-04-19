import React, { Component } from "react";
import axios from "axios";
import { API_URL } from "../constants";
import BlogList from './BlogList';
import '../App.css';

class Blog extends Component { 
    state = {
        blogs: []
    };

    componentDidMount() {
        this.resetState();
    }

    getBlogs = () => {
        axios.get(API_URL).then(res => this.setState({ blogs: res.data}))
    };

    resetState(){
        this.getBlogs();
    };

    render(){
        return (
            <div className="content-wrap">
                    <BlogList
                        blogs={this.state.blogs}
                        reserState={this.resetState}
                    />
            </div>

            // <div class="content-wrap">

            //     <div class="blog-container">
            //         <div class="blog-image ml-auto">
            //             <img src="./django.jpg" width="400" height="230" alt=""/>
            //         </div>

            //         <div class="blog-info text-left">
            //             <h2>Blog Topic</h2>
            //             <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            //         </div>
            //     </div>
            //     <div class="blog-splitter text-center">

            //     </div>

            //     <div class="blog-container">
            //         <div class="blog-image ml-auto">
            //             <img src="./django.jpg" width="400" height="230" alt=""/>
            //         </div>

            //         <div class="blog-info text-left">
            //             <h2>Blog Topic</h2>
            //             <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            //         </div>
            //     </div>

            //     <div class="blog-splitter">
            //     </div>

            //     <div class="blog-container">
            //         <div class="blog-image ml-auto">
            //             <img src="./django.jpg" width="400" height="230" alt=""/>
            //         </div>

            //         <div class="blog-info text-left">
            //             <h2>Blog Topic</h2>
            //             <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
            //         </div>
            //     </div>
            //     <div class="blog-splitter">

            //     </div>
            // </div>
        );
    }
}
export default Blog;

