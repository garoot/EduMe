import React from "react";
import React, { Component } from "react";
import axios from "axios";
import { Col, Container, Row } from "reactstrap";
import { API_URL } from "./constants/index";
import BlogList from './BlogList';
import './App.css';

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
            <div class="content-wrap">
                <BlogList
                    blogs={this.state.blogs}
                    reserState={this.resetState}
                />
            </div>
        )
    }

}
export default Blog;

