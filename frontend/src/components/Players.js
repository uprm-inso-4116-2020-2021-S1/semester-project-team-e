import React, {useState, useContext, useEffect} from 'react';
import Searchbar from './Searchbar';
import { Container, Card, Row, Col, Spinner } from 'react-bootstrap';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faFrown} from '@fortawesome/free-solid-svg-icons';
import PlayerPreview from './PlayerPreview';
import {AuthContext} from './AuthContext';
import axios from 'axios';


function Players() {
    const [state, setState] = useContext(AuthContext);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [player, setPlayer] = useState([]);

    useEffect(() => {
        const getPlayers = async () => {
            setIsLoading(true);
            await axios.get('http://localhost:5000/player')
                .then((response) => {
                    setPlayer(response.data.Players);
                    setIsError(false);
                })
                .catch(() => setIsError(true));
            setIsLoading(false);
        }
        getPlayers()
    }, [player]);

    if (isLoading) {
        return (
            <Container align="center">
                <h1>Loading...</h1>
                <Spinner animation="border"/>
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
            if (player.length === 0) {
                return (
                    <Container align="center" className="m-2">
                        <h1>No player found...</h1>
                    </Container>
                )
            } else {
                return (
                    <div>
                        <Container>
                            <Searchbar title="Players" placeholder="Search Players"/>
                            {player.map(team => (
                                <PlayerPreview playerID={player.player} playerName={player.player_name} team_name={player.team_name} />
                            ))}
                        </Container>
                    </div>
                )
            }
        }
    }
}

export default Players