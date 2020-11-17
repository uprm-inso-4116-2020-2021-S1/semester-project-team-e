import React from 'react';
import { Row, Col, Button, Modal, Form } from 'react-bootstrap'
import { LineChart, Line, BarChart,Bar, PieChart, Pie, Cell, Legend , CartesianGrid, XAxis, YAxis, Tooltip, } from 'recharts';

function SoccerTeamForm(props) {
    return (
        <Modal show={props.show} onHide={props.handleClose} animation="false">
            <Modal.Header closeButton>
                <Modal.Title>New statistic entry</Modal.Title>
            </Modal.Header>
            <Modal.Body>
                <Form> 
                    <Form.Group controlId="year">
                        <Form.Label>Date:</Form.Label> 
                        <Form.Control type="date"/>
                    </Form.Group>
                    <fieldset>
                        <Form.Group >
                            <Form.Label>
                                Match Result:
                            </Form.Label>
                            <Row>
                                <Col>
                                    <Form.Check type="radio" label="Won" name="formHorizontalRadios" id="formHorizontalRadios1"/>
                                </Col>
                                <Col>
                                    <Form.Check type="radio" label="Lost" name="formHorizontalRadios" id="formHorizontalRadios2"/>
                                </Col>
                                 <Col>
                                    <Form.Check type="radio" label="Draw" name="formHorizontalRadios" id="formHorizontalRadios2"/>
                                </Col>
                            </Row>
                        </Form.Group>
                    </fieldset>
                    <Form.Group controlId="goals_for">
                        <Form.Label>Goals for:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="goals_allowed">
                        <Form.Label>Goals Allowed:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="shots">
                        <Form.Label>Shots:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="shots_on_goal">
                        <Form.Label>Shots on Goal:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="saves">
                        <Form.Label>Saves:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="passes">
                        <Form.Label>Passes:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="possesions">
                        <Form.Label>Possesions:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="fouls">
                        <Form.Label>Fouls:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Button type="submit" variant="primary" onClick={props.handleClose}>
                        Submit
                    </Button>
                </Form>
            </Modal.Body>
        </Modal>
    );
}

function ReusableLineChart(props) {
    return (
        <LineChart className="mx-auto"
            width={500}
            height={300}
            data={props.data}
            margin={{
            top: 5, right: 30, left: 20, bottom: 5,
            }}
        >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="year" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey={props.dataKey} stroke={props.stroke} activeDot={{ r: 8 }} strokeWidth={2}/>
        </LineChart>
    );
}

function SoccerTeamStatistics(props) {
    const COLORS = ['#00C49F', '#ff7300', '#0088FE'];

    return (
        <div>
           <Row className="m-2">
            <Col>
                <h3>Yearly Perferomace:</h3>
                <LineChart className="mx-auto"
                    width={500}
                    height={300}
                    data={props.yearlyPerformance}
                    margin={{
                    top: 5, right: 30, left: 20, bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="year" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Line type="monotone" dataKey="wins" stroke="#8884d8" activeDot={{ r: 8 }} strokeWidth={2}/>
                    <Line type="monotone" dataKey="draws" stroke="#82ca9d" strokeWidth={2}/>
                    <Line type="monotone" dataKey="losses" strokeWidth={2}/>
                </LineChart>
            </Col>
            <Col>
                <h3>Overall Perferomace</h3>
                <PieChart width={300} height={300} className="mx-auto">
                    <Pie dataKey="value" data={props.overallPerformance} cx={150} cy={150} outerRadius={100} fill="#82ca9d" label >

                    {
                        props.overallPerformance.map((entry, index) => (<Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />))
                    }
                    </Pie>
                    yearlyPerformance
                    <Tooltip />
                    <Legend/>
                </PieChart>
            </Col>
        </Row>
        <Row className="m-2">
            <Col>
                <h3>Averages:</h3>
                <BarChart
                    width={500}
                    height={300}
                    data={props.averages}
                    margin={{
                    top: 5, right: 30, left: 20, bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="average" fill="#82ca9d" />
                </BarChart>
            </Col>
            <Col>
                <h3>Goals for:</h3>
                <ReusableLineChart data={props.goalsFor} dataKey="goals_for" stroke="#ff7300"/>
            </Col>
        </Row>
        <Row className="m-2">
            <Col>
                <h3>Goals allowed:</h3>
                <ReusableLineChart data={props.goalsAllowed} dataKey="goals_allowed" stroke="#00C49F"/>
            </Col>
            <Col>
                <h3>Shots:</h3>
                <ReusableLineChart data={props.shots} dataKey="shots" stroke="#8884d8"/>
            </Col>
        </Row>
        <Row className="m-2">
            <Col>
                <h3>Shots on Goal:</h3>
                <ReusableLineChart data={props.shotsOnGoal} dataKey="shots_on_goal" stroke="#ff7300"/>
            </Col>
            <Col>
                <h3>Saves:</h3>
                <ReusableLineChart data={props.saves} dataKey="saves" stroke="#00C49F"/>
            </Col>
        </Row>
        <Row className="m-2">
            <Col>
                <h3>Passes:</h3>
                <ReusableLineChart data={props.passes} dataKey="passes" stroke="#82ca9d"/>
            </Col>
            <Col>
                <h3>Possesions:</h3>
                <ReusableLineChart data={props.possesions} dataKey="possesions" stroke="#ff7300"/>
            </Col>
        </Row>
        <Row className="m-2">
            <Col>
                <h3>Fouls:</h3>
                <ReusableLineChart data={props.fouls} dataKey="fouls" stroke="#00C49F"/>
            </Col>
        </Row>
        </div>
    )
}

export {SoccerTeamStatistics, SoccerTeamForm};
