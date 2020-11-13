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
                        <Form.Label>Year:</Form.Label> 
                        <Form.Control as="select">
                            <option>2015</option>
                            <option>2016</option>
                            <option>2017</option>
                            <option>2018</option>
                            <option>2019</option>
                            <option>2020</option>
                            <option>2021</option>
                        </Form.Control>
                    </Form.Group>
                    <Form.Row>
                        <Form.Group as={Col} controlId="wins">
                            <Form.Label>Wins:</Form.Label>
                            <Form.Control placeholder="0"/>
                        </Form.Group>
                        <Form.Group as={Col} controlId="losses">
                            <Form.Label>Losses:</Form.Label>
                            <Form.Control placeholder="0"/>
                        </Form.Group>
                        <Form.Group as={Col} controlId="draws">
                            <Form.Label>Draws:</Form.Label>
                            <Form.Control placeholder="0"/>
                        </Form.Group>
                    </Form.Row>
                    <Form.Group controlId="goals_for">
                        <Form.Label>Goals for:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="goals_allowed">
                        <Form.Label>Goals Allowed:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="goal_difference">
                        <Form.Label>Goal Difference:</Form.Label>
                        <Form.Control placeholder="0"/>
                    </Form.Group>
                    <Form.Group controlId="points">
                        <Form.Label>Points:</Form.Label>
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
                <h3>Goal Averages:</h3>
                <BarChart
                    width={500}
                    height={300}
                    data={props.goalAverages}
                    margin={{
                    top: 5, right: 30, left: 20, bottom: 5,
                    }}
                >
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Legend />
                    <Bar dataKey="average" fill="#82ca9d" />
                </BarChart>
            </Col>
            <Col>
                <h3>Yearly Goals:</h3>
                <LineChart className="mx-auto"
                    width={500}
                    height={300}
                    data={props.yearlyGoals}
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
                    <Line type="monotone" dataKey="goalDifference" stroke="#82ca9d" strokeWidth={2}/>
                    <Line type="monotone" dataKey="goalFor" stroke="#ff7300" strokeWidth={2}/>
                    <Line type="monotone" dataKey="goalAllowed" strokeWidth={2}/>
                </LineChart>
            </Col>
        </Row>
        </div>
    )
}

export {SoccerTeamStatistics, SoccerTeamForm};
