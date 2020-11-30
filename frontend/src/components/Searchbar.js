import React, {useState} from 'react';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faSearch} from '@fortawesome/free-solid-svg-icons';
import {Form, Row, Col, Button, Modal, Container} from 'react-bootstrap';
import {useForm} from 'react-hook-form';
import {Redirect} from 'react-router-dom';
import axios from "axios";
import TeamPreview from "./TeamPreview";

function Searchbar(props) {
     const { register, handleSubmit} = useForm();
     const [teamsData, setTeamsData] = useState([]);
     const [show, setShow] = useState(false);
     const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
     const onSubmit = async data => {
            await axios.get(`http://localhost:5000/team?keyword=${data.search}`)
            .then((response) => {
            if(response.data.Teams){
                console.log(response.data);
                setTeamsData(response.data.Teams)
                handleShow();
            }
                })
     }
     if(show){
         return(
             <Modal show={show} onHide={handleClose}>
            <Modal.Header closeButton>
            <Modal.Title>Results</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <div>
                    <Container>
                        {teamsData.map(team => (
                            <TeamPreview key={team.team} noLink={false} teamName={team.team_name}
                                         teamID={team.team} teamMemberLength={0}/>
                        ))}
                    </Container>
                </div>
            </Modal.Body>
        </Modal>
         )}

    return (
        <div>
            <Row>
                <Col>
                    <h1>{props.title}</h1>
                </Col>
                <Col xs="auto">
                    <div className="m-2">
                        <Form inline onSubmit={handleSubmit(onSubmit)}>
                            <Form.Control type="text" placeholder={props.placeholder} className="mr-sm-2" name="search" ref={register}/>
                            <Button variant="outline-success" type="submit"><FontAwesomeIcon icon={faSearch}/></Button>
                        </Form> 
                    </div>
                </Col>
            </Row>
        </div>
    )
}

export default Searchbar
