import React, {useState, useContext, useEffec} from 'react';
import Searchbar from './Searchbar';
import { Container, Card, Row, Col } from 'react-bootstrap';
import PlayerPreview from './PlayerPreview';


function Players() {
    const [state, setState] = useContext(AuthContext);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [player, setPlayer] = useState({});

    useEffect(() => {
        const getTeams = async () => {
            setIsLoading(true);
            await axios.post('http://localhost:5000/player', {username: state.name})
                .then((response) => {
                    setPlayer(response.data.Teams);
                    setIsError(false);
                })
                .catch(() => setIsError(true));
            setIsLoading(false);
        }
    }, []);

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
            if (myTeams.length === 0) {
                return (
                    <Container align="center" className="m-2">
                        <h1>No teams found...</h1>
                    </Container>
                )
            } else {
                return (
                    <div>
                        <Container>
                            <Searchbar title="Players" placeholder="Search Players"/>
                            {teamsData.map(team => (
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
