import React from 'react';
import {Container} from 'react-bootstrap';
import Searchbar from '../components/Searchbar';
import TeamPreview from '../components/TeamPreview';

function Teams() {
    const dummyData = [
        { teamName: 'Los Coquis', teamID: 2, sportName: 'soccer', teamMemberLength: 8},
        { teamName: 'Bravos de Ponce', teamID: 3, sportName: 'soccer', teamMemberLength: 12},
        { teamName: 'Cangrejeros', teamID: 4, sportName: 'soccer', teamMemberLength: 10},
        { teamName: 'Gurabo FC', teamID: 6, sportName: 'soccer', teamMemberLength: 14},
    ]

    return (
        <div>
            <Container>
                <Searchbar title="Teams" placeholder="Search Teams"/>
                {dummyData.map(team => (
                    <TeamPreview key={team.teamID} noLink={false} teamName={team.teamName} teamID={team.teamID} teamMemberLength={team.teamMemberLength}/>
                ))}
            </Container>   
        </div>
    )
}

export default Teams
