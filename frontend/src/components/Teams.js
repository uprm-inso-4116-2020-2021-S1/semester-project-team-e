import React from 'react';
import {Container, Card, Row, Col, ListGroup} from 'react-bootstrap';
import Searchbar from '../components/Searchbar';
import {Link} from 'react-router-dom';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFutbol} from '@fortawesome/free-solid-svg-icons';

function TeamPreview(props) {
    const {teamID, teamName, teamMemberLength} = props;

    return (
        <Card as={Link} to={"team/" + teamID}  className="my-3" style={{textDecoration: 'none'}}>
             <Card.Header>
                <h5>   <FontAwesomeIcon icon={faFutbol} className="mr-1"/> {teamName}</h5>
                <hr/>
                <Row>
                    <Col>
                        Member count: {teamMemberLength}
                    </Col>
                </Row>
             </Card.Header>
         </Card>
    )
}

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
                    <TeamPreview key={team.teamID} teamName={team.teamName} teamID={team.teamID} teamMemberLength={team.teamMemberLength}/>
                ))}
            </Container>   
        </div>
    )
}

export default Teams
