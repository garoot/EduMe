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
                            <div className="blog-image">
                                <img src={blog.blog_picture} width="400" height="230" alt="" />
                            </div>

                            <div className="blog-info text-left">
                                <div className="blog-info-topic-wrap">

                                </div>
                                <div className="blog-info-topic">
                                    <h2>{blog.blog_title}</h2>
                                </div>
                                
                                {/* <p>{blog.description}</p> */}
                                <div className="blog-info-description">
                                    <p>{blog.blog_description}</p>
                                </div>
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
