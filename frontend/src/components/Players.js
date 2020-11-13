import React from 'react';
import Searchbar from './Searchbar';
import { Container, Card, Row, Col } from 'react-bootstrap';
import {Link} from 'react-router-dom';

function PlayerPreview(props) {
    const {playerID, playerName, position} = props;

    return (
        <Card as={Link} to={"player/" + playerID}  className="my-3" style={{textDecoration: 'none'}}>
             <Card.Header>
                <h5>{playerName}</h5>
                <hr/>
                <Row>
                    <Col>
                        Position: {position}
                    </Col>
                </Row>
             </Card.Header>
         </Card>
    )
}

function Players() {
    return (
        <div>
            <Container>
                <Searchbar title="Players" placeholder="Search Players"/>
                <PlayerPreview playerID={2} playerName={"Jerry Bassat"} position={"Goalie"} />
            </Container>
        </div>
    )
}

export default Players
