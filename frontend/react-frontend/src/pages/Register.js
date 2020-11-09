import React, { Component } from 'react';
import { Row, Col, FormGroup, Label, Input, Button } from 'reactstrap';
import axios from 'axios'

class Register extends Component {

    state = {
        username: '',
        fullName: '',
        email: '',
        password: ''
    }

     handleChange = event => {
    this.setState({
        [event.target.name]: event.target.value,
        [event.target.name]: event.target.value,
        [event.target.name]: event.target.value,
        [event.target.name]: event.target.value
    });
  }

    handleSubmit = event => {
        event.preventDefault();
        axios.post(`/register`, {
            username: this.state.username,
            full_name: this.state.fullName,
            email: this.state.email,
            password: this.state.password
        }, {
            headers: {
                'Content-Type': 'application/json'
            }
        })
          .then(res => {
            console.log(res);
            console.log(res.data);
            console.log(res.status);
      })

    }

    render() {
        const styles = {
            registerBox:{
                borderRadius:4,
                backgroundColor:'#ffffff',
                boxShadow:'0 30px 60px 0 rgba(0,0,0,0.3)',
                color:'black',
                paddingTop:20,
                paddingBottom:20
            },
            registerButton:{
                backgroundColor:'#0a1325',
                color:'#ffffff'
            },
            link:{
                color:'#203BAD'
            }
          };
        return <Row type="flex" justify="center" style={{ minHeight: '100vh', minWidth:300, alignContent:'center' }}>
            <Col span={8} style={styles.registerBox}>
            <h4 className="text-center">Register</h4>
                <form onSubmit={this.handleSubmit}>
                    <FormGroup>
                        <Label for="username">Username</Label>
                        <Input type="text" name="username" id="username" placeholder="Enter username" onChange={this.handleChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label for="fullName">Full Name</Label>
                        <Input type="text" name="fullName" id="fullName" placeholder="Ful Name" onChange={this.handleChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label for="email">Email</Label>
                        <Input type="email" name="email" id="email" placeholder="Enter email address" onChange={this.handleChange}/>
                    </FormGroup>
                    <FormGroup>
                        <Label for="password">Password</Label>
                        <Input type="password" name="password" id="password" placeholder="Enter password" onChange={this.handleChange}/>
                    </FormGroup>

                    <Button
                        block
                        type="primary"
                        type="submit"
                        className="register-form-button"
                        style={styles.registerButton}
                    >Register
                    </Button>
                </form>
            </Col>
        </Row>
    }
}
export default Register;