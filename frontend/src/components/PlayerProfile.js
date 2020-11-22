import React, {useContext} from 'react';
import { Container, Row, Col, Nav, Button } from 'react-bootstrap';
import {AuthContext} from './AuthContext';
import PlayerStatisticsContent from './player_statistics/PlayerStatisticsContent';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBalanceScale } from '@fortawesome/free-solid-svg-icons';

function PlayerProfile() {
    const [state, setState] = useContext(AuthContext);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [playerData, setPlayerData] = useState({});

    useEffect(() => {
        const fetchPlayerData = async () => {
            setIsLoading(true)
            await axios.get(`http://localhost:5000/player`)
                .then((response) => {
                    setPlayerData(response.data.Player[0]);
                    setIsError(false);
                })
                .catch(() => setIsError(true));
            setIsLoading(false)
        }
        fetchPlayerData();
    }, []);

    if (isLoading) {
        return (
            <Container align="center">
                <h1>Loading...</h1>
                <Spinner animation="border"/>
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

export default PlayerProfile