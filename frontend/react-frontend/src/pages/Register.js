import React, { Component } from 'react';
import { Row, Col, FormGroup, Label, Input, Button } from 'reactstrap';

class Register extends Component {
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
                <form>
                    <FormGroup>
                        <Label for="username">Username</Label>
                        <Input type="text" name="username" id="user" placeholder="Enter username" />
                    </FormGroup>
                    <FormGroup>
                        <Label for="exampleEmail">Email</Label>
                        <Input type="email" name="email" id="exampleEmail" placeholder="Enter email address" />
                    </FormGroup>
                    <FormGroup>
                        <Label for="examplePassword">Password</Label>
                        <Input type="password" name="password" id="examplePassword" placeholder="Enter password" />
                    </FormGroup>
                    <FormGroup>
                        <Label for="examplePassword">Confirm Password</Label>
                        <Input type="password" name="password" id="examplePassword" placeholder="Enter password again" />
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