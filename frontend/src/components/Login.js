import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import {Link} from 'react-router-dom';
import axios from 'axios';

function Login() {
      const [email, setEmail] = useState("");
      const [password, setPassword] = useState("");

      function validateForm() {
        return email.length > 0 && password.length > 0;
      }

        function handleSubmit(event){
            event.preventDefault();
            axios.post(`/register`, {
                email: email,
                password: password
            })
              .then(res => {
                console.log(res);
                console.log(res.data);
                console.log(res.status);
          })

        }

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
            color:'#ffffff',
            padding:"10px"
        }
      };
  return (
    <div className="Login" style={{ padding: '60px 0',width:'400px', margin: '0 auto' }}>
      <Form onSubmit={handleSubmit} style={styles.loginBox}>
      <h4 className="text-center">Login</h4>
        <Form.Group size="text" controlId="email" style={{padding:"10px"}}>
          <Form.Label>Email</Form.Label>
          <Form.Control
            autoFocus
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>
        <Form.Group size="text" controlId="password" style={{padding:"10px"}}>
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </Form.Group>
        <Button block size="lg" type="submit" disabled={!validateForm()} style={styles.loginButton}>
          Login
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
      </Form>
    </div>
  )
}

export default Login
