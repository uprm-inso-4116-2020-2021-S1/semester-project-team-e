import React from 'react';
import { Container, Card, Row, Col } from 'react-bootstrap';
import {Link} from 'react-router-dom';

function PlayerPreview(props) {
    const {playerID, playerName, position} = props;

    return (
        <Card as={Link} to={"/player/" + playerID}  className="my-3" style={{textDecoration: 'none'}}>
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

export default PlayerPreview;
