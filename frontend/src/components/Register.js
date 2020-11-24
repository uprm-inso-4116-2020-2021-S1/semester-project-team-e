import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import {Link} from 'react-router-dom';
import axios from 'axios';

function Login() {
      const [email, setEmail] = useState("");
      const [password, setPassword] = useState("");
      const [fullName, setFullName] = useState("");
      const [username, setUsername] = useState("");

      function validateForm() {
        return email.length > 0 && password.length > 0;
      }

      // function handleSubmit(event) {
      //   event.preventDefault();
      // }
        function handleSubmit(event){
            event.preventDefault();
            axios.post(`/register`, {
                username: username,
                full_name: fullName,
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
            color:'#ffffff',
            padding:"10px"
        }
      };
  return (
    <div className="Login" style={{ padding: '60px 0',width:'400px', margin: '0 auto' }}>
      <Form onSubmit={handleSubmit} style={styles.registerBox}>
      <h4 className="text-center">Register</h4>
        <Form.Group size="text" controlId="email" style={{padding:"10px"}}>
          <Form.Label>Email</Form.Label>
          <Form.Control
            autoFocus
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </Form.Group>
          <Form.Group size="text" controlId="formName" style={{padding:"10px"}}>
          <Form.Label>Full Name</Form.Label>
          <Form.Control
            autoFocus
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
          />
        </Form.Group>
        <Form.Group size="text" controlId="formUsername" style={{padding:"10px"}}>
          <Form.Label>Username</Form.Label>
          <Form.Control
            autoFocus
            value={username}
            onChange={(e) => setUsername(e.target.value)}
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
        <Button block size="lg" type="submit" disabled={!validateForm()}  style={styles.registerButton}>
          Register
        </Button>
      </Form>
    </div>
  )
}

export default Login
