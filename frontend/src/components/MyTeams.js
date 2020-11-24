import React, {useState, useContext, useEffect, useRef} from 'react';
import {Redirect} from 'react-router-dom';
import {Container, Col, Row, Button, Modal, Form} from 'react-bootstrap';
import Searchbar from '../components/Searchbar';
import TeamPreview from '../components/TeamPreview';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faPlus, faTrash} from '@fortawesome/free-solid-svg-icons';
import {AuthContext} from './AuthContext';
import {useForm, Controller} from 'react-hook-form';
import axios from 'axios';

function MyTeams() {
    const [state] = useContext(AuthContext);
    const [show, setShow] = useState(false);
    const [newTeam, setNewTeam] = useState({});
    const isInitialMount = useRef(true);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    useEffect(() => {
        const addTeam = async () => {
            await axios.post('http://localhost:5000/team', newTeam)
                .then((reponse) => {})
                .catch((error) => {})
        }

        if (isInitialMount.current) {
            isInitialMount.current = false;
        } else {
            addTeam();
        }
    }, [newTeam])

    const dummyData = [
        { teamName: 'Los Coquis', teamID: 2, sportName: 'soccer', teamMemberLength: 8},
        { teamName: 'Gurabo FC', teamID: 6, sportName: 'soccer', teamMemberLength: 14},
    ];

    const AddTeamForm = () => {
        const {control, handleSubmit} = useForm();

        const onSubmit = data => {
            data.username = state.name;
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
                    {dummyData.map(team => (
                        <Row key={team.teamID}>
                            <Col>
                                <TeamPreview  teamName={team.teamName} teamID={team.teamID} teamMemberLength={team.teamMemberLength}/>
                            </Col>                        
                            <Col xs="auto" className="align-self-center">
                                <Button variant="light"><FontAwesomeIcon icon={faTrash}/></Button>
                            </Col>
                        </Row>
                    ))}
                </Container>    
            </div>
        )
    } else {
        return <Redirect to="/login"/>
    }
    
}

export default MyTeams
