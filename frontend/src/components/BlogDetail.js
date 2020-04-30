import React, { Component } from "react";
import '../App.css';
import './prism.css';
import Prism from "prismjs";
// import Prism from './prism.js';
// import parse from 'html-react-parser';
import Sticky from 'react-stickynode';
import ShareLinks  from "./ShareLinks";
import MetaTags from 'react-meta-tags';
import Comments from './Comments';
import { BLOG_COMMENTS_API_URL } from "../constants";
import axios from "axios";

// import './prism.js';
// import CKEditor from '@ckeditor/ckeditor5-react';

class BlogDetail extends Component {
    state = {
        blog: null,
        content: null,
        comments: [],
        
    };
    componentDidMount() {
        // this.setState({comments: this.props.blog.comments})
        Prism.highlightAll();
        this.resetState();


    }

    getBlogComments = () => {

        const blogcomment_api_url = `${BLOG_COMMENTS_API_URL}`;
        axios.get(blogcomment_api_url+`1`).then(res => this.setState({ comments: res.data }))
    };

    resetState() {
        this.getBlogComments();
    };
    // displayContent(){
    //     parse()
    // }
    render() {
        // var parse = require('html-react-parser');
        const blog = this.props.blog;
        const temp_content = this.props.blog.content;
        // const content = toString(temp_content);
        return (

            
            <div className="article-wrap">
                <head>
                    <MetaTags>
                        <title>Hello</title>
                        <meta charset="UTF-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0, user-scalable=yes, target-densityDpi=device-dpi" />
                    </MetaTags>
                </head>
                {/* <link rel="stylesheet" href="/path/to/styles/default.css" /> */}
                {/* <script src="./prism.js"></script> */}
                <div className="article-left">
                    <ShareLinks/>
                    {/* <div className="article-left-wrapper">
                        <Sticky className="share-logos" top={100} bottomBoundary={652}>
                            <ul className="share-links" >
                                <div className="share-link">
                                    <Link>
                                        <img className="" src={require("./static/facebook.svg")} width="55" height="55" alt="" />
                                    </Link>
                                </div>

                                <div className="share-link">
                                    <Link>
                                        <img className="" src={require("./static/whatsapp.svg")} width="55" height="55" alt="" />
                                    </Link>
                                </div>

                                <div className="share-link">
                                    <Link>
                                        <img className="" src={require("./static/twitter.svg")} width="55" height="55" alt="" />
                                    </Link>
                                </div>

                                <div className="share-link">
                                    <Link>
                                        <img className="" src={require("./static/linkedin.svg")} width="55" height="55" alt="" />
                                    </Link>
                                </div>    

                            </ul>
                        </Sticky>                    
                    </div> */}
                </div>

                <div className="article-mid">
                    <header className="article-entry">
                        <div className="entry-top">
                            <div className="entry-top-left">
                                <img className="" src={require("./static/logo28.png")} width="135" height="30" alt="" />
                            </div>
                            <div className="entry-top-mid">
                                {blog.publish_date}
                            </div>
                            <div className="entry-top-right">
                                <img className="" src={require("./static/tag.svg")} width="30" height="30" alt="" />
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
                        <img src={blog.blog_picture} width="100%" alt="" />
                    </div>
                    <div className="article-content">
                        <div dangerouslySetInnerHTML={{ __html: temp_content }}></div>
                        {/* {parse(this.props.blog.content)} */}
                    </div>
                    <pre className="">
                        <code className="language-javascript">
                            {`const foo = 'foo';
const bar = 'bar';
console.log(foo + bar);
`}
                        </code>
                    </pre>
                    {/* card for author background and bio */}
                    <div className="author-bio"></div>

                    <div className="comments-wrapper">
                        <h3>Comments</h3>
                        <Comments 
                            comments={this.state.comments} 
                        />
                    </div>

                </div>

                <div className="article-right">
                    <Sticky top={90} bottomBoundary={0}>
                        <div className="about-article">
                            <img className="" src={require("./static/author.svg")} width="40" height="40" alt="" />

                        </div>
                    </Sticky>
                    <Sticky top={100} bottomBoundary={150}>
                        <div className="about-article-cover">
                        </div>


                    </Sticky>
                </div>
                



                {/* <script src="prism.js"></script> */}
            </div>
            
                    
        );
    }
}
export default BlogDetail;
