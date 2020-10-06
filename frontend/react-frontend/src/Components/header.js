import React, { Component } from 'react';

class Header extends Component {
    render() {
        return (
    <header className="masthead mt-auto">
        <div className="inner">
            <h3 className="masthead-brand">Sports Tracking (*tittle in progress)</h3>
            <nav className="nav nav-masthead justify-content-center">
                <a className="nav-link active" href="#">Home</a>
                <a className="nav-link" href="#">Sports</a>
                <a className="nav-link" href="#">Teams</a>
                <a className="nav-link" href="#">Log in/ Sign In</a>
                <a className="nav-link" href="#">Contact</a>
            </nav>
        </div>
    </header>
);
    }
}
export default Header;