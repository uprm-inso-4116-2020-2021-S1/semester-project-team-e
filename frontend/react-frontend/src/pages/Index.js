import React, { Component } from 'react';
import {Link } from "react-router-dom";
import Header from "../Components/header"
import './Index.css';

class Index extends Component {
    render() {
        return <div className="text-center">
            <div className="cover-container d-flex h-100 p-3 mx-auto flex-column">
                <Header/>

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