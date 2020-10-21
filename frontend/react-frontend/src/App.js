import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';

import Index from './pages/Index';
import Login from './pages/Login';
import Register from './pages/Register';

function App() {
  return (
    <main>
      <BrowserRouter>
        <Switch>
          <Route path="/" component={Index} exact />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
        </Switch>
      </BrowserRouter>
    </main>
  );
}

export default App;
