import React, {useState} from 'react';
import {Card, Row, Col, Container} from 'react-bootstrap';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFutbol} from '@fortawesome/free-solid-svg-icons';
import TeamPreview from "./TeamPreview";

function TeamCompare(props) {
    const [teamToCompare, setTeamToCompare] = useState();

    const TeamComparison = (props) => {
        return (
            <Container>
                <h1>{props.team1.teamName} VS {props.team2.teamName}</h1>
            </Container>
        );
    }

    const TeamChooser = (props) => {
        const dummyData = [
        { teamName: 'Los Coquis', teamID: 2, sportName: 'soccer', teamMemberLength: 8},
        { teamName: 'Bravos de Ponce', teamID: 3, sportName: 'soccer', teamMemberLength: 12},
        { teamName: 'Cangrejeros', teamID: 4, sportName: 'soccer', teamMemberLength: 10},
        { teamName: 'Gurabo FC', teamID: 6, sportName: 'soccer', teamMemberLength: 14},
    ];
        return (
            <div>
                 {dummyData.map(team => (
                     <div key={team.teamID} onClick={() => setTeamToCompare(team)}>
                        <TeamPreview noLink={true} key={team.teamID} teamName={team.teamName} teamID={team.teamID} teamMemberLength={team.teamMemberLength}/>
                    </div>
                ))}
            </div>
        );
    }

   if (teamToCompare) {
       return <TeamComparison team1={props.team} team2={teamToCompare}/>
   } else {
       return <TeamChooser/>
   }
}

export default TeamCompare
