import { Link } from 'react-router-dom';
import Sticky from 'react-stickynode';
import React from "react";
import '../App.css';
import './prism.css';


function ShareLinks(){
    return(
        <div className="article-left-wrapper">
            <Sticky className="share-logos" top={100} bottomBoundary={652}>
                <ul className="share-links" >
                    <div className="share-link">
                        <Link>
                            <img className="" src={require("./static/facebook.svg")} width="48" height="48" alt="" />
                        </Link>
                    </div>

                    <div className="share-link">
                        <Link>
                            <img className="" src={require("./static/instagram.svg")} width="46" height="46" alt="" />
                        </Link>
                    </div>
                    {/* <div className="share-link">
                        <Link>
                            <img className="" src={require("./static/whatsapp.svg")} width="55" height="55" alt="" />
                        </Link>
                    </div> */}

                    <div className="share-link">
                        <Link>
                            <img className="" src={require("./static/twitter.svg")} width="48" height="48" alt="" />
                        </Link>
                    </div>
    

                    {/* <div className="share-link">
                        <Link>
                            <img className="" src={require("./static/linkedin.svg")} width="55" height="55" alt="" />
                        </Link>
                    </div> */}

                </ul>
            </Sticky>
        </div>
    );
    
}
export default ShareLinks;