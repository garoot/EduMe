import React, { Component } from 'react'
import { NEWS_LETTER_EMAIL_LIST } from "../constants";
import axios from "axios";

export default class NewsLetter extends Component {
    constructor(props){
        super(props)
        this.state = {
            emails: [],
            new_email: null,
            response: null,
            is_new: false,
            posted: false,

        }
        this.baseState = this.state
    }


    componentDidMount(){
        //set the new email
        // this.setState({new_email: this.props.email})
        //retrieve all emails from server
        this.get_email_list();

        

        this.check_email_list()


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
        this.get_email_list()    
        const new_email = this.state.new_email

        const emails = this.state.emails
        let found = false
        // const found = emails.some(obj => toString(obj.email) === new_email)
        // found = emails.forEach(function(email){
        //     if (email.email===new_email){
        //         found = true
        //     }
        // })

        for (var i = 0, len = emails.length; i < len; i++) {
            if (emails[i].email === new_email) {
                found = true
            }        
        }
        if (found) {
            this.setState({ response: 'Already here..', is_new: false })

        } else {
            this.setState({ is_new: true })
        }
        // possible check method..
        // const arr = [{ id: 1, username: 'fred' }, { id: 2, username: 'bill' }, { id: 3, username: 'ted' }];

        // function add(arr, name) {
        //     const { length } = arr;
        //     const id = length + 1;
        //     const found = arr.some(el => el.username === name);
        //     if (!found) arr.push({ id, username: name });
        //     return arr;
        // }
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

    //instantly check if email is already in the list
    handleChange = event => {
        // first, might need to reset this.state.response
        this.setState({ new_email: event.target.value });
        // then check_emaillist()
        // this.check_email_list()

    };

    handleSubmit = event => {
        // event.preventDefault()
        let new_email = this.state.new_email
        const err_message = null
        //if there's a new email prompted..
        this.check_email_list()

        if (new_email){
            const is_new = this.state.is_new

            if (is_new) {
                //axios post
                try {
                    axios.post(NEWS_LETTER_EMAIL_LIST, {
                        email: new_email
                    }).then(function (response) {
                        console.log(response);
                    }).catch(error => 
                        
                        this.setState({ response: '', posted: false })
                    )
                        // .then(res => this.setState({ response: res.data }))
                    
                }
  
                catch (error) {
                    if (error.response){
                        this.setState({ response: error.response.status, posted: false })
                        err_message = error.response.status
                    } else {
                        console.log(error.response);
                    }
                }
                // axios.post(NEWS_LETTER_EMAIL_LIST, {
                //         email: new_email
                // })
                //     .then(res => this.setState({ response: res.data.error.mes }))
                //     .catch(function (error) {
                //         console.log(error.response);
                //     });
                // setState of this.state.response to 'Subscribed Successfully'
                if (!err_message){
                    this.setState({ response: 'Subscribed Successfully', posted: true })

                } else {
                    this.setState({ response: 'LMAO is this your email?', posted: false })
                }
                // setState of this.state.posted to True
            } 
            else {
                this.setState({ response: 'Already Subscribed My Love :) ' })
            }
        }

    }

    respond(){
        const response = this.state.response
        const is_new = this.state.is_new
        const posted = this.state.posted
        // if (is_new){
        //     return (
        //         <span>{this.state.new_email}</span>
        //     )
        // }

        if (is_new && posted) {
            // return response value
            return(<span>{response}</span>)

        } else if (response && is_new){
            return(<span>{response}</span>)

        } else if(response && !is_new){
            return (<span>{response}</span>)

        }
    }

    render() {

        return (
            <div className="footer-left-component">
                <div className="footer-left-text">
                    <h6 className="footer-left-h6">Subscribe for exclusive offers</h6>
                    <p className="footer-left-p">To receive exclusive offer on our products type your email</p>
                </div>

                <div className="footer-left-input">
                    <span>{this.respond()} </span>
                    <input type="text" name="email" value={this.state.new_email} placeholder="Email Address" onChange={this.handleChange} />
                    <button className="email-subscribe btn btn-primary" type="submit" onClick={this.handleSubmit} onBlur="">Subscribe</button>

                    {/* response either 'Already Exists' or 'Subscribed' or '' */}
                </div>

            </div>
            // emails.map(email =>
            //     (
            //         <span>{email.email}   </span>

            //     )

            // )
        )
    }
}
