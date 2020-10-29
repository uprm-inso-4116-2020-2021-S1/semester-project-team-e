import React from 'react';
import { Link } from 'react-router-dom';

const TeamPreview = (props) => {
    const {teamName, teamInfo, sport} = props;

    return (
        <div className="container" onClick={() => console.log(teamName)}>
            <div className="row">
                <div class="col-sm">
                    {teamName}
                </div>
                <div class="col-sm">
                    {teamInfo}
                </div>
                <div class="col-sm">
                    {sport}
                </div>
            </div>
        </div>
    );
}

export default TeamPreview;