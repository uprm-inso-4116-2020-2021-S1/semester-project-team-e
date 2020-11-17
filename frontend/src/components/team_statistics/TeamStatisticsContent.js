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
        {name:'Goal Allowed', average: 7}, 
        {name:'Goals for', average: 6}, 
        {name: 'Shots', average: 12},
        {name: 'Shots on goal', average: 10},
        {name: 'Saves', average: 5},
        {name: 'Passes', average: 20},
        {name: 'Posessions', average: 15},
        {name: 'Fouls', average: 3},
    ];
    const yearlyPerformanceDummy= [
        {year: 2016, wins: 3, losses: 2, draws: 1}, 
        {year: 2017, wins: 2, losses: 2, draws: 0}, 
        {year: 2018, wins: 2, losses: 1, draws: 2}, 
        {year: 2019, wins: 4, losses: 2, draws: 1},
        {year: 2020, wins: 2, losses: 3, draws: 0},
    ];
    const goalsForDummy = [
        {year: 2016, goals_for: 5}, 
        {year: 2017, goals_for: 2}, 
        {year: 2018, goals_for: 3}, 
        {year: 2019, goals_for: 6}, 
        {year: 2020, goals_for: 4}, 
    ];
    const goalsAllowedDummy= [
        {year: 2016, goals_allowed: 13}, 
        {year: 2017, goals_allowed: 9}, 
        {year: 2018, goals_allowed: 7}, 
        {year: 2019, goals_allowed: 8}, 
        {year: 2020, goals_allowed: 14}, 
    ];
    const shotsDummy= [
        {year: 2016, shots: 11}, 
        {year: 2017, shots: 5}, 
        {year: 2018, shots: 7}, 
        {year: 2019, shots: 12}, 
        {year: 2020, shots: 8}, 
    ];
    const shotsOnGoalDummy= [
        {year: 2016, shots_on_goal: 10}, 
        {year: 2017, shots_on_goal: 3}, 
        {year: 2018, shots_on_goal: 6}, 
        {year: 2019, shots_on_goal: 8}, 
        {year: 2020, shots_on_goal: 12}, 
    ];
    const savesDummy= [
        {year: 2016, saves: 7}, 
        {year: 2017, saves: 2}, 
        {year: 2018, saves: 2}, 
        {year: 2019, saves: 5}, 
        {year: 2020, saves: 6}, 
    ];
    const passesDummy= [
        {year: 2016, passes: 7}, 
        {year: 2017, passes: 5}, 
        {year: 2018, passes: 3}, 
        {year: 2019, passes: 7}, 
        {year: 2020, passes: 4}, 
    ];
    const possesionsDummy= [
        {year: 2016, possesions: 6}, 
        {year: 2017, possesions: 3}, 
        {year: 2018, possesions: 4}, 
        {year: 2019, possesions: 6}, 
        {year: 2020, possesions: 4}, 
    ];
    const foulsDummy= [
        {year: 2016, fouls: 7}, 
        {year: 2017, fouls: 9}, 
        {year: 2018, fouls: 5}, 
        {year: 2019, fouls: 5}, 
        {year: 2020, fouls: 11}, 
    ];

    return (
        <Container>
            <StatisticForm/>
            <AddStatisticBtn/>
            <SoccerTeamStatistics 
                yearlyPerformance={yearlyPerformanceDummy} 
                overallPerformance={overallPerformanceDummy} 
                averages={goalAveragesDummy} 
                goalsFor={goalsForDummy}
                goalsAllowed={goalsAllowedDummy}
                shots={shotsDummy}
                shotsOnGoal={shotsOnGoalDummy}
                saves={savesDummy}
                passes={passesDummy}
                possesions={possesionsDummy}
                fouls={foulsDummy}
            />
        </Container>
    )
}

export default TeamStatisticsContent;