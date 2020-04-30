import React, { Component } from "react";
import '../App.css';
import {Link} from 'react-router-dom';

class BlogList extends Component{
    state = {
        blogs: []
    }
    render() {
        const blogs = this.props.blogs;
        return (
            
            blogs.map(blog => 
                (
                    // <BlogDetail blog_id={blog.blog_id}/>

                    //onClick trigger retrieveBlogDetail() 
                    <Link to={`/blog/${blog.id}`}>
                        <div className="blog-container">
                            <div className="blog-image ml-auto">
                                <img src={blog.blog_picture} width="400" height="230" alt="" />
                            </div>

                            <div className="blog-info text-left">
                                <h2>{blog.blog_title}</h2>
                                {/* <p>{blog.description}</p> */}
                                 <p>{blog.blog_description}</p>
                            </div>
                        </div>
                        <div className="blog-splitter text-center">
                        </div>
                    </Link>
                    // <button onClick={blog => { this.setState({blog:blog})} } >


                    // </button>
                        

                
                )
            )
        );
    }
}
export default BlogList;
