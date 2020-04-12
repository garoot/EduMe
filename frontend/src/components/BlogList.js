import React, { Component } from "react";
import '../App.css';

class BlogList extends Component{
    render() {
        const blogs = this.props.blogs;
        return (
            blogs.map(blog => 
                (
                <div>
                    <div className="blog-container">
                        <div className="blog-image ml-auto">
                            <img src= {require("./static/django.jpg")} width="400" height="230" alt=""/>
                        </div>

                        <div className="blog-info text-left">
                            <h2>{blog.blog_title}</h2>
                            {/* <p>{blog.description}</p> */}
                            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                        </div>
                    </div>
                    <div className="blog-splitter text-center">
                    </div>
                </div>

                
                )
            )
        );
    }
}
export default BlogList;