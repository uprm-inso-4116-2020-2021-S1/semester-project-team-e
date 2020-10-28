import React, { Component } from 'react';
import {Link } from "react-router-dom";
import './Index.css';

class Index extends Component {
    render() {
        return <div className="text-center">
            <div className="cover-container d-flex h-100 p-3 mx-auto flex-column">
                <header className="masthead mb-auto">
                    <div className="inner">
                        <h3 className="masthead-brand">Sports Tracking</h3>
                        <nav className="nav nav-masthead justify-content-center">
                            <a className="nav-link active" href="#">Home</a>
                            <Link className="nav-link" to="/listSports">Sports</Link>
                            <a className="nav-link" href="#">Teams</a>
                            <a className="nav-link" href="#">Players</a>
                            <Link className="nav-link" to="login">Log in/ Sign In</Link>
                        </nav>
                    </div>
                </header>

                <div role="main" className="inner cover">
                    <h1 className="cover-heading">Sports Tracker</h1>
                    <p className="lead">Follow your favorite local or national team in every sport. Look at the standings for teams or players's statitics and more.</p>
                    <p className="lead">
                        <a href="#" className="btn btn-lg btn-secondary">Learn more</a>
                    </p>
                </div>

                <footer className="mastfoot mt-auto">
                    <div className="inner">
                        <p>Cover template for <a href="https://getbootstrap.com/">Bootstrap</a>, by <a href="https://twitter.com/mdo">@mdo</a>.</p>
                    </div>
                </footer>
            </div>
        </div>
    }
}

export default Index;