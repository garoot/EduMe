import React, { Component } from "react";
import axios from "axios";
import { API_URL, BLOG_DETAIL_API_URL , BLOG_COMMENTS_API_URL} from "../constants";
import BlogList from './BlogList';
import BlogDetail from './BlogDetail';

import '../App.css';

class GetBlogs extends Component {
    state = {
        blogs: []
    };

    componentDidMount() {
        this.resetState();
    }

    getBlogs = () => {
        axios.get(API_URL).then(res => this.setState({ blogs: res.data }))
    };

    resetState(){
        this.getBlogs();
    };

    render(){
        return (
            <div className="bloglist-wrap">
                <h3>Blogs</h3>
                <BlogList
                    blogs={this.state.blogs}
                    resetState={this.resetState}
                />
            </div>
        );
    }
}
export { GetBlogs };


class GetBlogDetail extends Component {
    state = {
        blog: [],
        comments:[]

    };

    componentDidMount() {

        const { match: { params } } = this.props;
        // saved in constants/index
        const blog_api_url = `${BLOG_DETAIL_API_URL}`;
        const blogcomment_api_url = `${BLOG_COMMENTS_API_URL}`;

         //FIRST VALID SOLUTION
        //passed from BlogList to App to here
        const blog_id = `${params.blogId}`;
        // fetching a blog and its comments
        axios.get(blog_api_url+blog_id).then(res => this.setState({ blog: res.data, comments: res.data.comments }));
        ///////////////////////////////////////////
         

    }


    render() {
        return (
            <div>
                <BlogDetail
                    //pass the retrieved blog  
                    //and its commentsto BlogDetail
                    blog={this.state.blog}
                    comments={this.state.comments}
                />
            </div>
        );
    }
}
export { GetBlogDetail };


