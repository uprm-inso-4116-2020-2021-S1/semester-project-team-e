import React, {useContext} from 'react';
import { Container, Row, Col, Nav, Button } from 'react-bootstrap';
import {AuthContext} from './AuthContext';
import PlayerStatisticsContent from './player_statistics/PlayerStatisticsContent';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBalanceScale } from '@fortawesome/free-solid-svg-icons';

function PlayerProfile() {
    const [state, setState] = useContext(AuthContext);

    return (
        <Container>
            <div>
            <Row>
                <Col>
                    <h1>Jerry Bassat</h1>
                </Col>
                <Col className="m-2 d-flex justify-content-end">
                    <Button>Compare <FontAwesomeIcon icon={faBalanceScale}/></Button>
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
