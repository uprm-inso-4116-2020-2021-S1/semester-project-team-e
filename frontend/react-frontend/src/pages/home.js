import React, { Component } from 'react';

import Header from '../Components/header';
import Footer from '../Components/footer';

class home extends Component {
    render() {
        return (
        <>
        <div class = "text-center">
        <div className="cover-container d-flex h-100 p-3 mx-auto flex-column">
		<Header />
                <main role="main" className="inner-cover">
                    <div class="cov">
                    <h1 className="cover-heading">Sports Tracker</h1>
                    <p className="lead">Follow your favorite local or national team in every sport. Look at the
                        standings for teams, players's statitics and more.</p>
                    <p className="lead">
                        <a href="#" className="btn btn-lg btn-secondary">Learn more</a>
                    </p>
                </div>
                </main>
        </div>
        <Footer />
        </div>
        </>
);
    }
}
export default home;