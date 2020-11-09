import React, { Component } from 'react';
import {Link} from "react-router-dom";

class Header extends Component {
    render() {
        const styles = {
            header: {
                width: '70em'
            }
          };
        return (
    <header className="masthead mt-auto" style={styles.header}>
        <div className="inner">
            <h3 className="masthead-brand">Sports Tracking </h3>
            <nav className="nav nav-masthead justify-content-center">
                <Link className="nav-link" to="/">Home</Link>
                <Link className="nav-link" to="/listSports">Sports</Link>
                <Link className="nav-link" to="/teams">Teams</Link>
                <Link className="nav-link" to="/listPlayers">Players</Link>
                <Link className="nav-link" to="login">Log in/ Sign In</Link>
            </nav>
        </div>
    </header>
);
    }
}
export default Header;