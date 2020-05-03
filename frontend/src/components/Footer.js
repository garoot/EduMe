
import React, { Component } from 'react';
import '../App.css';
import NewsLetter from './NewsLetter';


export default class Footer extends Component{
    state = {
        new_email: null,

    }

    render(){
        return (

            <footer className="footer">
                <div className="footer-section">
                    <div className="footer-wrap">

                        <div className="footer-left">
                            <NewsLetter/>
                            {/* <div className="footer-left-component">
                                <div className="footer-left-text">
                                    <h6 className="footer-left-h6">Subscribe for exclusive offers</h6>
                                    <p className="footer-left-p">To receive exclusive offer on our products type your email</p>
                                </div>

                                <div className="footer-left-input">
                                    <input type="text" name="email" value={this.state.new_email} placeholder="Email Address" onChange={this.handleChange}/>
                                    <input className="email-subscribe btn btn-primary" type="submit" value="Subscribe" />
                                </div>

                            </div> */}
                        </div>

                        <div className="footer-right text-center">
                            <div className="footer-right-left text-left">
                                <h6>About Us</h6>
                                <h6>Contact Us</h6>
                                <h6>Policies</h6>
                            </div>
                            <div className="footer-right-right-wrapper text-left">
                                <h6>Our Courses</h6>
                                <h6>Our Blogs</h6>
                                <h6>Terms and Conditions</h6>
                            </div>
                        </div>
                    </div>
                </div>
                {/* The Footer Bottom Section  */}
                <div className="footer-bottom">
                    {/* The Footer Brand */}
                    <div className="footer-bottom-left ">
                        <div className="footer-bottom-left-wrapper">
                            <div className="footer-logo-wrapper text-right">
                                <div>
                                    <a className="footer-logo " href="">
                                        <img src={require("./static/logo32.png")} width="109" height="20" alt="" />
                                    </a>
                                </div>

                            </div>
                            <div className="footer-rights-wrapper text-left">
                                <div>
                                    <span className="footer-copyright text-left"> &copy;
                                <script>document.write(new Date().getFullYear())</script>
                                CoursaTech. All Rights Reserved
                            </span>
                                </div>

                            </div>

                        </div>
                    </div>

                    <div className="footer-bottom-right">
                        <div className="social-media-links">
                        </div>
                    </div>

                    {/* The Footer Links Wrapper */}
                    <div className="footer-social-links">
                        <div className="footer-links">
                        </div>
                    </div>

                </div>
            </footer>
        );


    }


    }
    
   