import React, { Component } from 'react';
import {Link} from "react-router-dom";

class Header extends Component {
    render() {
        return (
    <header className="masthead mt-auto">
        <div className="inner">
            <h3 className="masthead-brand">Sports Tracking </h3>
            <nav className="nav nav-masthead justify-content-center">
                <Link className="nav-link active" to="/">Home</Link>
                <Link className="nav-link" to="/listSports">Sports</Link>
                <a className="nav-link" href="#">Teams</a>
                <Link className="nav-link" to="/listPlayers">Players</Link>
                <Link className="nav-link" to="login">Log in/ Sign In</Link>
            </nav>
        </div>
    </header>
);
    }
}
export default Header;