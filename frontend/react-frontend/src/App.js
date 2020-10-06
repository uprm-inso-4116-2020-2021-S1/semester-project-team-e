import React, { useState, useEffect }from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import home from './pages/home'

function App() {

  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);
  return (
      <Router>
        <Switch>
          <Route exact path="/" component={home} />
        </Switch>
      </Router>
  );
}

export default App;
