import React, {useState, useContext, useEffect} from 'react';
import {useParams} from 'react-router-dom';
import { Container, Row, Col, Nav, Card, Button, Modal, Spinner } from 'react-bootstrap';
import {AuthContext} from './AuthContext';
import TeamStatisticsContent from './team_statistics/TeamStatisticsContent';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBalanceScale, faPlus, faFrown } from '@fortawesome/free-solid-svg-icons';
import TeamCompare from './TeamCompare';
import PlayerPreview from './PlayerPreview';
import axios from 'axios';

function ManagerContent(props) {
    const {managers} = props;

    const ManagerPreview = (props) => {
        return (
            <Card className="my-3">
                <Card.Header>{props.name}</Card.Header>
                    <Card.Body>
                    <Card.Text>
                        <p>Email: {props.email}</p>
                    </Card.Text>
                </Card.Body>
            </Card>
        )
    }

    if(managers.length === 0) {
        return (
            <Container align="center" className="m-2">
                <h1>No managers found</h1>
            </Container>
        )
    } else {
        return (
        <Col className="m-2">
            {managers.map(manager => (
                <ManagerPreview name={manager.full_name} email={manager.email}/>
            ))}
        </Col>
        )
    }
}

function PlayersContent(props) {
    const {players, state} = props;

    const AddPlayerBtn = () => {
        if (state.name) {
            return (
                <Row className="m-2 d-flex justify-content-end">
                    <Button>
                        Add Player <FontAwesomeIcon icon={faPlus}/>
                    </Button>
                </Row>
            );
        } else {
            return(
                <div></div>
            );
        }
    }

    return (
        <Container className="m-2">
            <AddPlayerBtn/>
            {/* {players.map(player => ( */}
                {/* <PlayerPreview playerID={} playerName={} position={} /> */}
            {/* ))} */}
            <PlayerPreview playerID={2} playerName={"Mario Diaz"} position={"Goalie"}/>
            <PlayerPreview playerID={2} playerName={"Jose Joestar"} position={"Goalie"}/>
        </Container>
    );
}

function TeamProfile() {
    const tabs = {
        MANAGER: 'manager',
        PLAYERS: 'players',
        STATISTICS: 'statistics'
    };

    let {id} = useParams();
    let [tab, setActiveTab] = useState(tabs.STATISTICS);
    const [state, setState] = useContext(AuthContext);
    const [show, setShow] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [teamData, setTeamData] = useState({});
    const [statistics, setStatistics] = useState([]);

    useEffect(() => {
        const fetchTeamData = async () => {
            setIsLoading(true)
            await axios.get(`http://localhost:5000/team/${id}`)
                .then((response) => {
                    if(response.data.Teams.length === 0) {
                        setIsError(true);
                    } else {
                        setTeamData(response.data.Teams[0]);
                        setStatistics(response.data.Teams[0].team_statistics)
                        setIsError(false);
                    }})
                .catch(() => setIsError(true));
            setIsLoading(false)
        }

        fetchTeamData();
    }, []);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const CompareModal = () => {
        return (
        <Modal size="lg" show={show} onHide={handleClose} backdrop="static">
            <Modal.Header closeButton>
                <Modal.Title>Compare Team:</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <TeamCompare team={{teamName: "Los coquis", teamID: 2}}/>
            </Modal.Body>
            <Modal.Footer>
                <Button variant="secondary" onClick={handleClose}>
                    Close
                </Button>
                <Button variant="primary" onClick={handleClose}>
                    Save Changes
                </Button>
            </Modal.Footer>
        </Modal>
        );
    }

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
            let content;
            switch (tab) {
                case tabs.STATISTICS:
                        content = <TeamStatisticsContent state={state} statistics={statistics}/>
                    break;
                case tabs.MANAGER:
                    content = <ManagerContent managers={teamData.managers}/>
                    break;
                case tabs.PLAYERS:
                    content = <PlayersContent state={state}/>
                    break;
                default:
                    break;
            }

            return (
                <Container>
                    <CompareModal/>
                    <div>
                    <Row>
                        <Col>
                            <h1>{teamData.team_name}</h1>
                        </Col>
                        <Col className="m-2 d-flex justify-content-end">
                            <Button onClick={() => handleShow()}>Compare <FontAwesomeIcon icon={faBalanceScale}/></Button>
                        </Col>
                    </Row>
                    <Row>
                        <Col>
                            <h4>{teamData.team_info}</h4>
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
    }
}

export default TeamProfile