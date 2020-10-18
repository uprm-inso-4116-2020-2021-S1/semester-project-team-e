import React, { Component } from 'react';
import { Row, Col, FormGroup, Label, Input, Button } from 'reactstrap';

class Login extends Component {
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
                </form>
            </Col>
        </Row>
    }
}
export default Login;