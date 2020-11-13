import './App.css';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom'; 
import Header from './components/Header';
import Footer from './components/Footer';
import Home from './components/Home';
import Teams from './components/Teams';
import Players from './components/Players';
import TeamProfile from './components/TeamProfile';
import PlayerProfile from './components/PlayerProfile';
import {AuthProvider} from './components/AuthContext';

function App() {
  return (
    <Router>
      <div>
        <AuthProvider>
          <Header/>
          <Switch>
            <Route exact path="/">
              <Home title="Sport Statistics Tracker"/>
            </Route>
            <Route path="/players">
              <Players/>
            </Route>
            <Route path="/teams">
              <Teams/>
            </Route>
            <Route path="/team/:id">
              <TeamProfile/>
            </Route>
            <Route path="/player/:id">
              <PlayerProfile/>
            </Route>
            <Route path="/login">
              <Home title="Login"/>
            </Route>
            <Route path="/register">
              Register
            </Route>
          </Switch>
          {/* <Footer/> */}
        </AuthProvider>
      </div>
    </Router>
  );
}

export default App;
