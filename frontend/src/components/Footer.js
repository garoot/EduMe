
import React from 'react';
import '../App.css';

export default function Footer() {
    return (

        <footer className="footer">
            <div className="footer-section">
                <div className="footer-wrap">

                    <div className="footer-left">
                        <div className="footer-left-component">
                            <h6>Subscribe for exclusive offers</h6>
                            <p>To receive exclusive offer on our products type your email</p>
                            <input type="email" name="" value="Enter Email"/>
                            <input className="email-subscribe btn btn-primary" type="submit" value="Subscribe"/>
                        </div>
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
                        <a className="footer-logo text-right" href="">
                            <img src={require("./static/logo32.png")} width="109" height="20" alt="" />
                        </a>
                        <span className="footer-copyright"> &copy;
                    <script>document.write(new Date().getFullYear())</script>
                    CoursaTech. All Rights Reserved
                </span>
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

