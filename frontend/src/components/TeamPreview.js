import React from 'react';
import {Card, Row, Col} from 'react-bootstrap';
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

export default TeamPreview
