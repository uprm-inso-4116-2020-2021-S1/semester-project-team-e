import React, { Component } from 'react';
import { Row, Col, FormGroup, Label, Input, Button } from 'reactstrap';
import {Link } from "react-router-dom";
import axios from "axios";

class Login extends Component {

    state = {
        email: '',
        password: ''
    }

     handleChange = event => {
    this.setState({
        [event.target.name]: event.target.value,
        [event.target.name]: event.target.value
    });
  }



    handleSubmit = event => {
        // const onSuccess = ({data}) => {
        //   setClientToken(data.token);
        //   this.setState({isLoading: false, isAuthorized: true});
        // };
        //
        // const onFailure = error => {
        //   console.log(error && error.response);
        //   this.setState({errors: error.response.data, isLoading: false});
        // };
        event.preventDefault();
        axios.post(`/login`, {
            email: this.state.email,
            password: this.state.password
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
          .then(res => {
            const accessToken = res.data.access_token
            console.log(res);
            console.log(res.data);
            console.log(res.status);
      })

    }

    render() {
        const styles = {
            loginBox:{
                borderRadius:4,
                backgroundColor:'#ffffff',
                boxShadow:'0 30px 60px 0 rgba(0,0,0,0.3)',
                color:'black',
                paddingTop:20,
                paddingBottom:20
            },
            loginButton:{
                backgroundColor:'#0a1325',
                color:'#ffffff'
            },
            link:{
                color:'#203BAD'
            }
          };
        return <Row type="flex" justify="center" style={{ minHeight: '100vh', minWidth:300, alignContent:'center' }}>
            <Col span={8} style={styles.loginBox}>
            <h4 className="text-center">Login</h4>
                <form>
                    <FormGroup>
                        <Label for="exampleEmail">Email</Label>
                        <Input type="email" name="email" id="exampleEmail" placeholder="Enter email address" />
                    </FormGroup>
                    <FormGroup>
                        <Label for="examplePassword">Password</Label>
                        <Input type="password" name="password" id="examplePassword" placeholder="Enter password" />
                    </FormGroup>

                    <Button
                        block
                        type="primary"
                        type="submit"
                        className="login-form-button"
                        style={styles.loginButton}
                    >Log in
                    </Button>
                    <div className="mt-4">
                        <div className="d-flex justify-content-center links">
                            <a class="link" style={styles.link} href="#">Forgot your password?</a>
                        </div>
                        <div className="d-flex justify-content-center links">
                            Don't have an account?
                            <Link className="nav-link" style={styles.link} to="/register" className="ml-2" >Sign Up</Link>
                        </div>
                    </div>
                </form>
            </Col>
        </Row>
    }
}
export default Login;