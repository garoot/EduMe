import React from 'react';
import {NavLink, Link} from 'react-router-dom';
import '../App.css';

function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg">
            

            <div className="navbar-brand">
                <Link to='/'>
                    <img src={require("./static/logo28.png")} width="185" height="35" alt="" />
                </Link>
            </div>
        

            <div className="collapse navbar-collapse">
                <ul className="navbar-nav ml-auto">
                    <div className="nav-buttonwrap">
                        <NavLink className="nav-link button" to="/">
                            Blogs
                        </NavLink>

                    </div>


                    {/* <li className="nav-item">
                        <a className="nav-link" href="#">Notifications<span className="sr-only">(current)</span></a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">My Cart</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">My Courses</a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">My Account</a>
                    </li> */}
                </ul>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent15"
                    aria-controls="navbarSupportedContent15" aria-expanded="false" aria-label="Toggle navigation"><span className="navbar-toggler-icon"></span>
                </button>
            </div>
        </nav>
    );
}

export default Navbar;