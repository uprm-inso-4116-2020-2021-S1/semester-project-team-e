import React from 'react';
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
        const fetchTeamData = async () => {
            setIsLoading(true)
            await axios.get(`http://localhost:5000/team`)
                .then((response) => {
                    setTeamsData(response.data.Teams);
                    setIsError(false);
                    })
                .catch(() => setIsError(true));
            setIsLoading(false)
        }

        fetchTeamData();
    }, []);
    var teamList = [];
    for(i=0; i < teamsData.length; i++){
      teamList.push({ teamName: teamsData.teamName, teamID: teamsData.teamID, sportName: teamsData.teamSports, teamMemberLength: teamsData.teamMemberLength});
    }
    // const dummyData = [
    //     { teamName: 'Los Coquis', teamID: 2, sportName: 'soccer', teamMemberLength: 8},
    //     { teamName: 'Bravos de Ponce', teamID: 3, sportName: 'soccer', teamMemberLength: 12},
    //     { teamName: 'Cangrejeros', teamID: 4, sportName: 'soccer', teamMemberLength: 10},
    //     { teamName: 'Gurabo FC', teamID: 6, sportName: 'soccer', teamMemberLength: 14},
    // ]

    return (
        <div>
            <Container>
                <Searchbar title="Teams" placeholder="Search Teams"/>
                {teamList.map(team => (
                    <TeamPreview key={team.teamID} noLink={false} teamName={team.teamName} teamID={team.teamID} teamMemberLength={team.teamMemberLength}/>
                ))}
            </Container>
        </div>
    )
}

export default Teams