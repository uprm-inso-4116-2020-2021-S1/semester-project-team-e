import React from 'react';
import {Container, Col, Row, Button} from 'react-bootstrap';
import Searchbar from '../components/Searchbar';
import TeamPreview from '../components/TeamPreview';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faPlus, faTrash} from '@fortawesome/free-solid-svg-icons';

function MyTeams() {
    const dummyData = [
        { teamName: 'Los Coquis', teamID: 2, sportName: 'soccer', teamMemberLength: 8},
        { teamName: 'Gurabo FC', teamID: 6, sportName: 'soccer', teamMemberLength: 14},
    ];

    return (
        <div>
           <Container>
                <Row>
                    <Col>
                        <h1>My Teams</h1>
                    </Col>
                    <Col className="m-2 d-flex justify-content-end">
                        <Button>Add Team <FontAwesomeIcon icon={faPlus}/></Button>
                    </Col>
                </Row>
                {dummyData.map(team => (
                    <Row key={team.teamID}>
                        <Col>
                            <TeamPreview  teamName={team.teamName} teamID={team.teamID} teamMemberLength={team.teamMemberLength}/>
                        </Col>                        
                        <Col xs="auto" className="align-self-center">
                            <Button variant="light"><FontAwesomeIcon icon={faTrash}/></Button>
                        </Col>
                    </Row>
                ))}
            </Container>    
        </div>
    )
}

export default MyTeams
