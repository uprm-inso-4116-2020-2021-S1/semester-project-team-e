import React, {useState} from 'react'
import { Container, Row, Button} from 'react-bootstrap'
import {SoccerTeamStatistics, SoccerTeamForm} from './SoccerTeamStatistics';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';

function TeamStatisticsContent(props) {
    const [show, setShow] = useState(false);

    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const AddStatisticBtn = () => {
        if (props.state.name) {
            return (
                <Row className="m-2 d-flex justify-content-end">
                    <Button onClick={handleShow}>
                        Add Statistics <FontAwesomeIcon icon={faPlus}/>
                    </Button>
                </Row>
            );
        } else {
            return(
                <div></div>
            );
        }
    }

    const StatisticForm = () => {
        return (
           <SoccerTeamForm handleClose={handleClose} show={show}/> 
        );
    }

    let overallPerformanceDummy = [
        { name: 'Wins', value: 3}, 
        { name: 'Loses', value: 2 }, 
        { name: 'Draws', value: 1 }, 
    ];
    const goalAveragesDummy = [
        {name: 'Difference', average: 2}, 
        {name:'Goal Allowed', average: 3}, 
        {name:'Goals for', average: 2}, 
        {name:'Goal', average:2}
    ];
    const yearlyPerformanceDummy= [
        {year: 2016, wins: 3, losses: 2, draws: 1}, 
        {year: 2017, wins: 2, losses: 2, draws: 0}, 
        {year: 2018, wins: 2, losses: 1, draws: 2}, 
        {year: 2019, wins: 4, losses: 2, draws: 1},
        {year: 2020, wins: 2, losses: 3, draws: 0},
    ];
    const yearlyGoalDummy = [
        {year: 2016, goalDifference: 2, goalAllowed: 3, goalFor: 3, goals: 1}, 
        {year: 2017, goalDifference: 3, goalAllowed: 1, goalFor: 1, goals: 2}, 
        {year: 2018, goalDifference: 4, goalAllowed: 1, goalFor: 1, goals: 1}, 
        {year: 2019, goalDifference: 2, goalAllowed: 4, goalFor: 3, goals: 1}, 
        {year: 2020, goalDifference: 2, goalAllowed: 2, goalFor: 2, goals: 2}, 
    ];

    return (
        <Container>
            <StatisticForm/>
            <AddStatisticBtn/>
            <SoccerTeamStatistics yearlyPerformance={yearlyPerformanceDummy} overallPerformance={overallPerformanceDummy} goalAverages={goalAveragesDummy} yearlyGoals={yearlyGoalDummy}/>
        </Container>
    )
}

export default TeamStatisticsContent;