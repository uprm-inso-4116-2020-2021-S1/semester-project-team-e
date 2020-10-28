import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';

import Index from './pages/Index';
import Login from './pages/Login';
import Register from './pages/Register';
import ListSport from "./pages/ListSport";
import ListPlayers from "./pages/ListPlayers";

function App() {
  return (
    <main>
      <BrowserRouter>
        <Switch>
          <Route path="/" component={Index} exact />
          <Route path="/login" component={Login} />
          <Route path="/register" component={Register} />
          <Route path="/listSports" component={ListSport}/>
          <Route path="/listPlayers" component={ListPlayers}/>
        </Switch>
      </BrowserRouter>
    </main>
  );
}

export default App;
