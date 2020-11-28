import React, {useContext, useState, useEffect} from 'react';
import { Container, Row, Col, Nav, Button } from 'react-bootstrap';
import {AuthContext} from './AuthContext';
import PlayerStatisticsContent from './player_statistics/PlayerStatisticsContent';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBalanceScale, faFrown } from '@fortawesome/free-solid-svg-icons';
import Axios from 'axios';
import { useParams } from 'react-router-dom';

function PlayerProfile() {
    const {id} = useParams();
    const [state, setState] = useContext(AuthContext);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [playerData, setPlayerData] = useState({});
    const [statistics, setStatistics] = useState([]);

    useEffect(() => {
        const fetchPlayerData = async () => {
            setIsLoading(true);
            await Axios.get(`http://localhost:5000/player/${id}`)
                .then((reponse) => {
                    if(Response.data.Players.length === 0) {
                        setIsError(true);
                    } else {
                        setPlayerData(reponse.data.Players[0]);
                        setStatistics(Response.data.Teams[0].player_statistics)
                        setIsError(false);
                    }})
                .catch(() => setIsError(true));
        }

        fetchPlayerData();
    }, [])

    if (isLoading) {
        return (
            <Container align="center" className="my-3">
                <FontAwesomeIcon icon={faFrown} size="9x"/>
                <h1>Something went wrong...</h1>
            </Container>
        )
    } else {
        if (isError) {
            return (
                <Container>
                    <Col align="center" className="my-3">
                        <FontAwesomeIcon icon={faFrown} size="9x"/>
                        <h1>Something went wrong...</h1>
                    </Col>
                </Container>
            )
        } else {
            return (
                <Container>
                    <div>
                    <Row>
                        <Col>
                            <h1>Mario Diaz</h1>
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
    }
}

export default PlayerProfile
