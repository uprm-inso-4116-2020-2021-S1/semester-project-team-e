import React from 'react';
import {Container,Jumbotron, Card, Row, Col, Button} from 'react-bootstrap';
import {Link} from 'react-router-dom'; 
import teamImg from '../images/volleyTeam.jpg';
import playerImg from '../images/soccerPlayer.jpg';

function Home(props) {
    return (
        <Container fluid>
            <Jumbotron className="m-3">
                <h1>{props.title}</h1>
                <p>
                    This is a simple hero unit, a simple jumbotron-style component for calling
                    extra attention to featured content or information.
                </p>
            </Jumbotron>
            <Container>
            <Row>
            <Col>
            <Card fluid>
                <Card.Img variant="top" src={playerImg} />
                <Card.Body>
                    <Card.Title>Discorver Players</Card.Title>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk of
                        the card's content.
                    </Card.Text>
                    <Button as={Link} to="/players" variant="primary">Explore Players</Button>
                </Card.Body>
            </Card>
            </Col>
            <Col>
            <Card fluid>
                <Card.Img variant="top" src={teamImg}/>
                <Card.Body>
                    <Card.Title>Discorver Teams</Card.Title>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk of
                        the card's content.
                    </Card.Text>
                    <Button as={Link} to="/teams" variant="primary">Explore Teams</Button>
                </Card.Body>
            </Card>
            </Col>
            </Row>
            </Container>

        </Container>
    )
}

export default Home
