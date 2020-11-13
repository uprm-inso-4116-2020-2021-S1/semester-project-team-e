import React, {useState, useContext} from 'react'
import { Container, Row, Col, Nav, Card } from 'react-bootstrap'
import {AuthContext} from './AuthContext';
import TeamStatisticsContent from './team_statistics/TeamStatisticsContent';

function ManagerContent() {
    return (
        <Col className="m-2">
                <Card className="my-3">
                    <Card.Img variant="top" src="" fluid/>
                    <Card.Header>Jerry Bassat</Card.Header>
                    <Card.Body>
                        <Card.Text>
                            <p>Email:</p>
                            <p>Phone number:</p>
                        </Card.Text>
                    </Card.Body>
                </Card>
                <Card className="my-3">
                    <Card.Img variant="top" src="" fluid/>
                    <Card.Header>Jerry Bassat</Card.Header>
                    <Card.Body>
                        <Card.Text>
                            <p>Email:</p>
                            <p>Phone number:</p>
                        </Card.Text>
                    </Card.Body>
                </Card>
        </Col>
    )
}

function PlayersContent() {
    return (
        <Col className="m-2">
                <Card className="my-3">
                    <Card.Img variant="top" src="" fluid/>
                    <Card.Header>Jose Martinez</Card.Header>
                    <Card.Body>
                        <Card.Text>
                            <p>Age:</p>
                            <p>Position:</p>
                        </Card.Text>
                    </Card.Body>
                </Card>
                <Card className="my-3">
                    <Card.Img variant="top" src="" fluid/>
                    <Card.Header>Mario Diaz</Card.Header>
                    <Card.Body>
                        <Card.Text>
                            <p>Age:</p>
                            <p>Position:</p>
                        </Card.Text>
                    </Card.Body>
                </Card>
        </Col>
    )
}

function TeamProfile() {
    const tabs = {
        MANAGER: 'manager',
        PLAYERS: 'players',
        STATISTICS: 'statistics'
    };

    let [tab, setActiveTab] = useState(tabs.STATISTICS);
    const [state, setState] = useContext(AuthContext);

    let content;
    switch (tab) {
        case tabs.STATISTICS:
            content = <TeamStatisticsContent state={state}/>
            break;
        case tabs.MANAGER:
            content = <ManagerContent/>
            break;
        case tabs.PLAYERS:
            content = <PlayersContent/>
            break;
        default:
            break;
    }

    return (
        <Container>
            <div>
            <Row>
                <Col>
                    <h1>Los Coquis</h1>
                </Col>
            </Row>
            <Row>
                <Col>
                    <h4>Team Info goes here </h4>
                </Col>
            </Row>
            </div>
            <Nav justify variant="tabs" defaultActiveKey="/home">
                <Nav.Item>
                    <Nav.Link eventKey="link-1" onClick={() => setActiveTab(tabs.STATISTICS)}>Statistics</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="link-2" onClick={() => setActiveTab(tabs.MANAGER)}>Managers</Nav.Link>
                </Nav.Item>
                <Nav.Item>
                    <Nav.Link eventKey="link-3" onClick={() => setActiveTab(tabs.PLAYERS)}>Players</Nav.Link>
                </Nav.Item>
            </Nav>
            {content}
        </Container>
    )
}

export default TeamProfile
