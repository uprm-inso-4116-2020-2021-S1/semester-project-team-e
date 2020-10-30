import React from 'react';
import { Link } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faCoffee, faFutbol } from '@fortawesome/free-solid-svg-icons'

const TeamPreview = (props) => {
    const {teamName, teamInfo, sport} = props;

    return (
        <div className="container p-2 mb-3 bg-secondary text-white text-center font-weight-bolder rounded border">
            <Link to="/" style={{ textDecoration: 'none' }}>
            <div className="row">
                <div class="col-sm text-uppercase">
                    {teamName}
                </div>
                <div class="col-sm">
                    {teamInfo}
                </div>
                <div class="col-sm">
                    <FontAwesomeIcon icon={faFutbol} />
                </div>
            </div>
            </Link>
        </div>
    );
}

export default TeamPreview;