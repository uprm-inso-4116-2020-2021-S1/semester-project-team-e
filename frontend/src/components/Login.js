import React, { useState, useContext, useEffect, useRef } from "react";
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import {Link, Redirect} from 'react-router-dom';
import axios from 'axios';
import {useForm, Controller} from 'react-hook-form';
import {AuthContext} from './AuthContext';

function Login() {
      const [state, setState] = useContext(AuthContext);
      const [loginData, setLoginData] = useState({});
      const [wrongLogin, setWrongLogin] = useState(false);
      const { control, handleSubmit } = useForm();
      const isInitialMount = useRef(true);

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

      const onSubmit = data => {
        setLoginData(data);
      }

      useEffect(() => {
        const login = async () => {
          await axios.post('http://localhost:5000/login', loginData)
            .then((response) => {
              setState({name:loginData.username, token:response.data.access_token});
            })
            .catch(() => {
              setWrongLogin(true);
            });
        };
        if (isInitialMount.current) {
            isInitialMount.current = false;
        } else {
            login();
        }
      },[loginData])


  return (
    <div className="Login" style={{ padding: '60px 0',width:'400px', margin: '0 auto' }}>
    {state.name && state.token && <Redirect to="/"/>}
      <Form onSubmit={handleSubmit(onSubmit)} style={styles.loginBox}>
      <h4 className="text-center">Login</h4>
        <Form.Group size="text" controlId="email" style={{padding:"10px"}}>
          <Form.Label>Username:</Form.Label>
          <Controller as={Form.Control}
            autoFocus
            name="username"
            control={control}
            defaultValue=""
          />
        </Form.Group>
        <Form.Group size="text" controlId="password" style={{padding:"10px"}}>
          <Form.Label>Password</Form.Label>
          <Controller as={Form.Control}
            type="password"
            name="password"
            control={control}
            defaultValue=""
          />
        </Form.Group>
        { wrongLogin && <div style={{color: "red"}} className="d-flex justify-content-center">Wrong username or password</div> }
        <Button block size="lg" type="submit" style={styles.loginButton}>
          Login
        </Button>
          <div className="mt-4">
            <div className="d-flex justify-content-center links">
                Don't have an account?
                <Link style={styles.link} to="/register" className="ml-2" >Sign Up</Link>
            </div>
          </div>
      </Form>
     </div>
  )
}

export default Login
