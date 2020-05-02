import React, { Component } from 'react'
import { NEWS_LETTER_EMAIL_LIST } from "../constants";
import axios from "axios";

export default class NewsLetter extends Component {
    state = {
        emails: [],
        new_email: null,
        response: null,
        new: false,

    }

    componentDidMount(){
        //set the new email
        // this.setState({new_email: this.props.email})
        //retrieve all emails from server
        this.get_email_list();

    }

    //..retrieving email list from database
    get_email_list(){
        axios.get(NEWS_LETTER_EMAIL_LIST)
        .then(res => this.setState({ emails: res.data }));

    }
    //..check if passed email already exists
    check_email_list(){
    //if new_email in emails, response='Already Subscribed'
    //if this.state.new is true, call add_new_email(this.state.new_email)

    }

    //..after checking again email list is negative, add new email
    // add_new_email = (new_email) => {
    //     axios.post(NEWS_LETTER_EMAIL_LIST, {
    //         params: {
    //             email: new_email,
    //         }
    //     }).then(res => this.setState({ response: res.data }))
    //
    // }
    handleChange = event => {
        this.setState({ new_email: event.target.value });
    };

    render() {
        const emails = this.state.emails
        return (
            <div className="footer-left-component">
                <div className="footer-left-text">
                    <h6 className="footer-left-h6">Subscribe for exclusive offers</h6>
                    <p className="footer-left-p">To receive exclusive offer on our products type your email</p>
                </div>

                <div className="footer-left-input">
                    <input type="text" name="email" value={this.state.new_email} placeholder="Email Address" onChange={this.handleChange} />
                    <input className="email-subscribe btn btn-primary" type="submit" value="Subscribe" />
                </div>

            </div>
            // emails.map(email =>
            //     (
            //         <span>{email.email}</span>
            //     )

            // )
        )
    }
}
