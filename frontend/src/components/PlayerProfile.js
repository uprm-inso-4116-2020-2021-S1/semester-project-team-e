import React, {useContext} from 'react';
import { Container, Row, Col, Nav } from 'react-bootstrap';
import {AuthContext} from './AuthContext';
import PlayerStatisticsContent from './player_statistics/PlayerStatisticsContent';

function PlayerProfile() {
    const [state, setState] = useContext(AuthContext);

    return (
        <Container>
            <div>
            <Row>
                <Col>
                    <h1>Jerry Bassat</h1>
                </Col>
            </Row>
            <Row>
                <Col>
                    <h4>Player Info goes here</h4>
                </Col>
            </Row>
            </div>
            <Nav justify variant="tabs" defaultActiveKey="/home">
                <Nav.Item>
                    <Nav.Link eventKey="link-1">Statistics</Nav.Link>
                </Nav.Item>
            </Nav>
            <PlayerStatisticsContent state={state}/>
        </Container>
    );
}

export default PlayerProfile
