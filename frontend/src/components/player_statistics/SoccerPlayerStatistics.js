import React from 'react';
import { Row, Col, Button, Modal, Form } from 'react-bootstrap';
import { LineChart, Line, BarChart,Bar, PieChart, Pie, Cell, Legend , CartesianGrid, XAxis, YAxis, Tooltip, } from 'recharts';

function SoccerPlayerForm(props) {
    return (
        <Modal show={props.show} onHide={props.handleClose} animation="false">
            <Modal.Header closeButton>
                <Modal.Title>New statistic entry</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form> 
                    <Form.Group controlId="Date">
                        <Form.Label>Date:</Form.Label> 
                        <Form.Control type="date" />
                    </Form.Group>
                    <fieldset>
                        <Form.Group >
                            <Form.Label>
                                Halve Number:
                            </Form.Label>
                            <Row>
                                <Col>
                                    <Form.Check type="radio" label="1" name="formHorizontalRadios" id="formHorizontalRadios1"/>
                                </Col>
                                <Col>
                                    <Form.Check type="radio" label="2" name="formHorizontalRadios" id="formHorizontalRadios2"/>
                                </Col>
                            </Row>
                        </Form.Group>
                    </fieldset>
                    <Form.Row>
                        <Form.Group as={Col} controlId="yellow_cards">
                            <Form.Label>Yellow Cards:</Form.Label>
                            <Form.Control placeholder="0"/>
                        </Form.Group>
                        <Form.Group as={Col} controlId="red_cards">
                            <Form.Label>Red Cards:</Form.Label>
                            <Form.Control placeholder="0"/>
                        </Form.Group>
                    </Form.Row>
                    <Form.Group controlId="goals">
                        <Form.Label>Goals:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="assists">
                        <Form.Label>Assists:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="saves">
                        <Form.Label>Saves:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="takles_won">
                        <Form.Label>Tackles Won:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Button type="submit" variant="primary" onClick={props.handleClose}>
                        Submit
                    </Button>
                </Form>
            </Modal.Body>
        </Modal>
    )
}

function SoccerPlayerStatistics(props) {
    return (
        <div>
            <Row className="m-2">
                <Col>
                    <h3>Yearly Average Performance:</h3>
                    <LineChart className="mx-auto"
                        width={500}
                        height={300}
                        data={props.yearlyAvgPerformance}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                    <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="year" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="goals" stroke="#8884d8" activeDot={{ r: 8 }} strokeWidth={2}/>
                        <Line type="monotone" dataKey="assists" stroke="#82ca9d" strokeWidth={2}/>
                        <Line type="monotone" dataKey="saves" strokeWidth={2}/>
                    </LineChart>
                </Col>
                <Col>
                   <h3>Yearly Average Penalties:</h3> 
                   <LineChart className="mx-auto"
                        width={500}
                        height={300}
                        data={props.yearlyAvgPenalty}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                    <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="year" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="yellow_cards" stroke="#8884d8" activeDot={{ r: 8 }} strokeWidth={2}/>
                        <Line type="monotone" dataKey="red_cards" stroke="#82ca9d" strokeWidth={2}/>
                    </LineChart>
                </Col>
            </Row> 
            <Row className="m-2">
                <Col>
                    <h3>Goals:</h3>
                    <BarChart
                        width={500}
                        height={300}
                        data={props.goals}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="date" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="goals" fill="#82ca9d" />
                    </BarChart>
                </Col>
                <Col>
                    <h3>Assists:</h3>
                    <BarChart
                        width={500}
                        height={300}
                        data={props.assists}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="date" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="assists" fill="#82ca9d" />
                    </BarChart>
                </Col>
            </Row>
            <Row className="m-2">
                <Col>
                    <h3>Saves:</h3>
                    <BarChart
                        width={500}
                        height={300}
                        data={props.saves}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="date" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="saves" fill="#82ca9d" />
                    </BarChart>
                </Col>
                <Col>
                    <h3>Tackles Won:</h3>
                    <BarChart
                        width={500}
                        height={300}
                        data={props.tacklesWon}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}
                    >
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="date" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="tacklesWon" fill="#82ca9d" />
                    </BarChart>
                </Col>
            </Row>
        </div>
    )
}

export {SoccerPlayerStatistics, SoccerPlayerForm}
