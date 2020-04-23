import React, { Component } from "react";
import '../App.css';
import CKEditor from '@ckeditor/ckeditor5-react';


class BlogDetail extends Component {
    state = {
        blog: null
    };
    
    render() {
        const blog = this.props.blog;
        return (

            <div className="article-wrap">

                <header className="article-entry">
                    <div className="entry-top">
                        <div className="entry-top-left">
                            <img className="" src={require("./static/logo28.png")} width="135" height="30" alt=""/>
                         </div>
                        <div className="entry-top-right">
                            {blog.publish_date}
                        </div>
                    </div>

                    <div className="article-title">
                        <h2>{blog.blog_title}</h2>
                    </div>
                    <div className="article-author">
                        <h5>{blog.full_name}</h5>
                    </div>
                </header>
                <div className="article-image">
                    <img src={blog.blog_picture} width="750" alt=""/>
                 </div>
                    <div className="article-content">
                        <div dangerouslySetInnerHTML={{ __html: this.props.blog.content }}></div>
                
                    </div>



            </div>
            
                    
        );
    }
}
export default BlogDetail;
