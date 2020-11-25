import React, {useState, useContext, useEffec} from 'react';
import {Container} from 'react-bootstrap';
import Searchbar from '../components/Searchbar';
import TeamPreview from '../components/TeamPreview';

function Teams() {
    const [state, setState] = useContext(AuthContext);
    const [show, setShow] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    const [isError, setIsError] = useState(false);
    const [teamsData, setTeamsData] = useState({});

    useEffect(() => {
        const getTeams = async () => {
            setIsLoading(true);
            await axios.post('http://localhost:5000/teams', {username: state.name})
                .then((response) => {
                    setTeamsData(response.data.Teams);
                    setIsError(false);
                })
                .catch(() => setIsError(true));
            setIsLoading(false);
        }
    }, []);

    if (isLoading) {
        return (
            <Container align="center">
                <h1>Loading...</h1>
                <Spinner animation="border"/>
            </Container>
        )
    } else {
        if (isError) {
            return (
                <Container>
                    <Col align="center" className="my-3">
                        <FontAwesomeIcon icon={faFrown} size="9x"/>
                        <h1>Something went wrong...</h1>
                    </Col>
                </Container>
            )
        } else {
            if (myTeams.length === 0) {
                return (
                    <Container align="center" className="m-2">
                        <h1>No teams found...</h1>
                    </Container>
                )
            } else {
                return (
                    <div>
                        <Container>
                            <Searchbar title="Teams" placeholder="Search Teams"/>
                            {teamsData.map(team => (
                                <TeamPreview key={team.team} noLink={false} teamName={team.team_name} teamID={team.team} teamMemberLength={0}/>
                            ))}
                        </Container>
                    </div>
                )
            }
        }
    }
}

export default Teams