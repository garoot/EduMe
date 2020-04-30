import React, { Component } from "react";
import axios from "axios";
import { API_URL, BLOG_DETAIL_API_URL } from "../constants";
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
            <div className="content-wrap">
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
        blog: {
        },

    };

    componentDidMount() {

        const { match: { params } } = this.props;
        // saved in constants/index
        const blog_api_url = `${BLOG_DETAIL_API_URL}`;
        // passed from BlogList to App to here
        const blog_id = `${params.blogId}`;
        // fetching..
        axios.get(blog_api_url+blog_id).then(res => this.setState({ blog: res.data }));
        }

    // retrieveBlogDetail = () => {
    //     const { match: { params } } = this.props;
    //     axios.get(`http://localhost:8000/api/blog/${params.blogId}`).then(res => this.setState({ blog: res.data }));
    // };

    // resetState() {
    //     this.retrieveBlogDetail();
    // };

    render() {
        return (
            <div className="content-wrap">
                <BlogDetail
                    blog={this.state.blog}
                    resetState={this.resetState}
                />
            </div>
        );
    }
}
export { GetBlogDetail };


