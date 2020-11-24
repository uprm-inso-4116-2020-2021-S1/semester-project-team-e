import React from 'react';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome';
import {faSearch} from '@fortawesome/free-solid-svg-icons';
import {Form, Row, Col, Button} from 'react-bootstrap';
import {useForm} from 'react-hook-form';

function Searchbar(props) {
     const { register, handleSubmit, watch, errors } = useForm();
     const onSubmit = data => console.log(data);

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
