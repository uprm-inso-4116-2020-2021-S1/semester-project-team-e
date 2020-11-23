import React, {useState} from 'react'
import { Container, Row, Button} from 'react-bootstrap'
import {SoccerTeamStatistics, SoccerTeamForm} from './SoccerTeamStatistics';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';

function TeamStatisticsContent(props) {
    const {statistics, state} = props;

    const [show, setShow] = useState(false);

    // Look up use callback
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);

    const AddStatisticBtn = () => {
        if (state.name) {
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
    const yearlyPerformanceDummy= [
        {year: 2016, wins: 3, losses: 2, draws: 1}, 
        {year: 2017, wins: 2, losses: 2, draws: 0}, 
        {year: 2018, wins: 2, losses: 1, draws: 2}, 
        {year: 2019, wins: 4, losses: 2, draws: 1},
        {year: 2020, wins: 2, losses: 3, draws: 0},
    ];

    let content;
    if (statistics.length === 0) {
        content = <Container align="center" className="m-2">
                       <h1>No Statistics found...</h1>
                  </Container>
    } else {
        let goalsFor =[], goalsAllowed = [], passes = [], possesions = [], saves = [], shots = [], shotsOnGoal = [], fouls = [];
        let averages = [
                {name:'Goal Allowed', average: 0}, 
                {name:'Goals for', average: 0}, 
                {name: 'Shots', average: 0},
                {name: 'Shots on goal', average: 0},
                {name: 'Saves', average: 0},
                {name: 'Passes', average: 0},
                {name: 'Posessions', average: 0},
                {name: 'Fouls', average: 0},
            ];

        statistics.forEach((statistic) => {
            const date = new Date(Date.parse(statistic.date));
            const year = date.getFullYear();

            goalsFor.push({year: year, goals_for: statistic.goals_for});
            averages[1].average += statistic.goals_for;

            goalsAllowed.push({year: year, goals_allowed: statistic.goals_allowed});
            averages[0].average += statistic.goals_allowed;

            passes.push({year: year, passes: statistic.passes});
            averages[5].average += statistic.passes;

            possesions.push({year: year, possesions: statistic.possession});
            averages[6].average += statistic.possession;

            saves.push({year: year, saves: statistic.saves});
            averages[4].average += statistic.saves;

            shots.push({year: year, shots: statistic.shots});
            averages[2].average += statistic.shots;

            shotsOnGoal.push({year: year, shots_on_goal: statistic.shots_on_goal});
            averages[3].average += statistic.shots_on_goal;

            fouls.push({year: year, fouls: statistic.fouls});
            averages[7].average += statistic.fouls;
        })

        averages.forEach(stat => stat.average /= statistics.length)

        content = <SoccerTeamStatistics 
                    yearlyPerformance={yearlyPerformanceDummy} 
                    overallPerformance={overallPerformanceDummy} 
                    averages={averages} 
                    goalsFor={goalsFor}
                    goalsAllowed={goalsAllowed}
                    shots={shots}
                    shotsOnGoal={shotsOnGoal}
                    saves={saves}
                    passes={passes}
                    possesions={possesions}
                    fouls={fouls}
                  />
    }

    return (
        <Container>
            <StatisticForm/>
            <AddStatisticBtn/>
            {content}
        </Container>
    )
}

export default TeamStatisticsContent;