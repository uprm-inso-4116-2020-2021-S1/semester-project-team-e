import React from 'react';
import Searchbar from './Searchbar';
import { Container, Card, Row, Col } from 'react-bootstrap';
import PlayerPreview from './PlayerPreview';

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
