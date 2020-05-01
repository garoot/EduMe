import React, { Component } from 'react'
import '../App.css';

export default class Comments extends Component {
    state = {
        comments : {}
    }

    render() {
        let temp_comments = []
        temp_comments = this.props.comments

        return (
            temp_comments.map(comment =>
                ( 
                    <div>
                        <div className="comment-wrapper text-center">
                            <div className="comment-left mr-auto">
                                <img
                                    src={require("./static/linkedin.svg")}
                                    width="55" height="55"
                                    alt=""
                                />
                            </div>
                            <div className="comment-right text-left mr-auto">
                                <div className="comment-header">
                                    <div className="comment-creator">
                                        <h4>{comment.full_name} - </h4> 
                                    </div>
                                    <div className="comment-created">
                                        <h7>{comment.created}</h7>
                                    </div>
                                </div>


                                {comment.text}

                            </div>
                        </div>
                        <div className="comment-spliiter"></div>

                    </div>
                    

        
                )
            )

        )
    }
}
