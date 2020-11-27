import React, {useState, useContext, useEffect, useRef} from 'react';
import {Redirect} from 'react-router-dom';
import {Container, Col, Row, Button, Modal, Form, Spinner} from 'react-bootstrap';
import TeamPreview from '../components/TeamPreview';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faPlus, faTrash, faFrown} from '@fortawesome/free-solid-svg-icons';
import {AuthContext} from './AuthContext';
import {useForm, Controller} from 'react-hook-form';
import axios from 'axios';


function MyTeams() {
    const [state] = useContext(AuthContext);
    const [show, setShow] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [myTeams, setMyTeams] = useState([]);
    const [newTeam, setNewTeam] = useState({});
    // const [teamIdToDelete, setTeamIdToDelete] = useState(70);
    const isInitialMount = useRef(true);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    useEffect(() => {
        const getMyTeams = async () => {
            setIsLoading(true);
            await axios.post('http://localhost:5000/manager/myteams', {username: state.name})
                .then((response) => {
                    setMyTeams(response.data.Teams);
                    setIsError(false);
                })
                .catch(() => setIsError(true));
            setIsLoading(false);
        }

        const addTeam = async () => {
            await axios.post('http://localhost:5000/team', newTeam)
                .then((response) => {})
                .catch((error) => {})
        }

        if (isInitialMount.current) {
            isInitialMount.current = false;
            getMyTeams();
        } else {
            addTeam();
            getMyTeams();
        }
    }, [newTeam]);

    // useEffect(() => {
        // const deleteTeam = async () => {
            // await axios.delete(`http://localhost:5000/team/${teamIdToDelete}`)
                // .then((response) => {})
                // .catch(() => setIsError(true));
        // }

        // if (isInitialMount.current) {
            // isInitialMount.current = false;
        // } else {
            // deleteTeam();
        // }
    // }, [teamIdToDelete])

    const AddTeamForm = () => {
        const {control, handleSubmit} = useForm();

        const onSubmit = data => {
            data.username = state.name;
            setNewTeam(data)
            console.log(data);
            handleClose();
        }

        return (
        <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
            <Modal.Title>New Team</Modal.Title>
            </Modal.Header>
            <Modal.Body>
               <Form onSubmit={handleSubmit(onSubmit)}>
                   <Form.Group>
                       <Form.Label>
                           Sport:
                       </Form.Label>
                        <Controller
                            as = {
                                <Form.Control as="select">
                                    <option>soccer</option>
                                </Form.Control>
                            }
                            defaultValue = "soccer"
                            name="sport_name"
                            control={control}
                         />
                   </Form.Group>
                   <Form.Group>
                       <Form.Label>
                           Team Name:
                       </Form.Label>
                       <Controller as={Form.Control} name="team_name" control={control} defaultValue="name"/>
                   </Form.Group>
                   <Form.Group>
                       <Form.Label>
                           Team Info:
                       </Form.Label>
                       <Controller as={Form.Control} name="team_info" control={control} defaultValue="info"/>
                   </Form.Group>
                    <Button variant="primary" type="submit">
                        Save Changes
                    </Button>
               </Form>
            </Modal.Body>
        </Modal>
        )
    }

    const TeamList = () => {
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
                        myTeams.map(team => (
                            <Row key={team.team}>
                                <Col>
                                    <TeamPreview teamName={team.team_name} teamID={team.team} teamMemberLength={0}/>
                                </Col>                        
                                <Col xs="auto" className="align-self-center">
                                    <Button variant="light"><FontAwesomeIcon icon={faTrash}/></Button>
                                </Col>
                            </Row>
                        ))
                    )
                }
            }
        }
    }

    if (state.name) {
        return (
            <div>
            <Container>
                    <AddTeamForm/>
                    <Row>
                        <Col>
                            <h1>My Teams</h1>
                        </Col>
                        <Col className="m-2 d-flex justify-content-end">
                            <Button onClick={handleShow}>Add Team <FontAwesomeIcon icon={faPlus}/></Button>
                        </Col>
                    </Row>
                    <TeamList myTeams={myTeams}/> 
                </Container>    
            </div>
        )
    } else {
        return <Redirect to="/login"/>
    }
    
}

export default MyTeams
