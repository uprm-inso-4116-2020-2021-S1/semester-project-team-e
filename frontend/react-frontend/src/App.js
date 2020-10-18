import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';

import Index from './pages/Index';
import Login from './pages/Login';

function App() {
  return (
    <main>
      <BrowserRouter>
        <Switch>
          <Route path="/" component={Index} exact />
          <Route path="/login" component={Login} />
        </Switch>
      </BrowserRouter>
    </main>
  );
}

export default App;
