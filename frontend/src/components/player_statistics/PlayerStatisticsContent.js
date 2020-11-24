import React, {useState} from 'react';
import { Container, Row, Button} from 'react-bootstrap';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import {SoccerPlayerStatistics, SoccerPlayerForm} from './SoccerPlayerStatistics';

function PlayerStatisticsContent(props) {
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
            <SoccerPlayerForm handleClose={handleClose} show={show} />
        );
    }

    const yearlyAvgPenaltyDummy = [
        { year: 2016, yellow_cards: 2, red_cards: 0 },
        { year: 2017, yellow_cards: 1, red_cards: 1 },
        { year: 2018, yellow_cards: 0, red_cards: 0 },
        { year: 2019, yellow_cards: 1, red_cards: 2 },
        { year: 2020, yellow_cards: 0, red_cards: 1 },
    ];
    const yearlyAvgPerformanceDummy= [
        { year: 2016, goals: 3, assists: 5, saves: 0 },
        { year: 2017, goals: 5, assists: 3, saves: 3 },
        { year: 2018, goals: 3, assists: 4, saves: 0 },
        { year: 2018, goals: 2, assists: 2, saves: 4 },
        { year: 2019, goals: 3, assists: 2, saves: 2 },
        { year: 2020, goals: 7, assists: 1, saves: 1 },
    ];
    const goalsDummy = [
        { date: "02/11/2016", halve: 1, goals: 1 },
        { date: "02/11/2016", halve: 2, goals: 3 },
        { date: "05/17/2017", halve: 1, goals: 2 },
        { date: "07/12/2018", halve: 1, goals: 3 },
        { date: "05/15/2018", halve: 1, goals: 2 },
        { date: "06/14/2018", halve: 1, goals: 1 },
        { date: "04/15/2019", halve: 1, goals: 2 },
        { date: "011/15/2019", halve: 1, goals: 1 },
        { date: "06/11/2020", halve: 1, goals: 3 },
    ];
    const assistsDummy = [
        { date: "02/11/2016", halve: 1, assists: 3 },
        { date: "02/11/2016", halve: 2, assists: 2 },
        { date: "05/17/2017", halve: 1, assists: 4 },
        { date: "07/12/2018", halve: 1, assists: 5 },
        { date: "05/15/2018", halve: 2, assists: 3 },
        { date: "06/14/2018", halve: 1, assists: 1 },
        { date: "04/15/2019", halve: 2, assists: 3 },
        { date: "11/15/2019", halve: 1, assists: 2 },
        { date: "06/11/2020", halve: 1, assists: 2 },
    ];
    const savesDummy = [
        { date: "02/11/2016", halve: 1, saves: 2 },
        { date: "02/11/2016", halve: 2, saves: 3 },
        { date: "05/17/2017", halve: 1, saves: 0 },
        { date: "07/12/2018", halve: 1, saves: 4 },
        { date: "05/15/2018", halve: 2, saves: 1 },
        { date: "06/14/2018", halve: 1, saves: 2 },
        { date: "04/15/2019", halve: 2, saves: 4 },
        { date: "11/15/2019", halve: 1, saves: 3 },
        { date: "06/11/2020", halve: 1, saves: 2 },
    ];
    const tacklesWonDummy = [
        { date: "02/11/2016", halve: 1, tacklesWon: 3 },
        { date: "02/11/2016", halve: 2, tacklesWon: 2 },
        { date: "05/17/2017", halve: 1, tacklesWon: 2 },
        { date: "07/12/2018", halve: 1, tacklesWon: 3 },
        { date: "05/15/2018", halve: 2, tacklesWon: 4 },
        { date: "06/14/2018", halve: 1, tacklesWon: 2 },
        { date: "04/15/2019", halve: 1, tacklesWon: 3 },
        { date: "11/15/2019", halve: 2, tacklesWon: 1 },
        { date: "06/11/2020", halve: 1, tacklesWon: 1 },
    ];

    return (
        <Container>
            <StatisticForm/>
            <AddStatisticBtn/>
            <SoccerPlayerStatistics 
                yearlyAvgPerformance={yearlyAvgPerformanceDummy} 
                yearlyAvgPenalty={yearlyAvgPenaltyDummy} 
                goals={goalsDummy} 
                saves={savesDummy} 
                assists={assistsDummy} 
                tacklesWon={tacklesWonDummy}
            />
        </Container> 
    );
}

export default PlayerStatisticsContent
