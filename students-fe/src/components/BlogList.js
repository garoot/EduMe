import React, { Component } from "react";
import './App.css';

class BlogList extends Component{
    render() {
        const blogs = this.props.blogs;
        return (
            blogs.map(blog => 
                (

                <div className="blog-container">
                    <div className="blog-image ml-auto">
                        <img src="./django.jpg" width="400" height="230" alt=""/>
                    </div>

                    <div className="blog-info text-left">
                        <h2>{blog.blog_title}</h2>
                        <p>{blog.blog_description}</p> 
                    </div>
                </div>
                
                )
            )
        );
    }
}
export default BlogList;