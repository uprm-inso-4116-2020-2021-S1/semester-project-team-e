import React, {useState, useEffect, useRef} from 'react';
import {BarChart, Bar, Cell, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer} from 'recharts';
import {Container, Spinner} from 'react-bootstrap';
import TeamPreview from "./TeamPreview";
import axios from 'axios';

function TeamChooser(props) {
        const [teams, setTeams] = useState([]);

        useEffect(() => {
            const getTeams = async () => {
                await axios.get('http://localhost:5000/team')
                    .then((response) => {
                        setTeams(response.data.Teams);
                        console.log(teams);
                    })
                    .catch(() => {});
            }
            getTeams();
        }, [])

        return (
            <div>
                 {teams.map(team => (
                     <div key={team.team} onClick={() => props.setTeamToCompare(team)}>
                        <TeamPreview noLink={true} teamName={team.team_name} teamID={team.team} teamMemberLength={0}/>
                    </div>
                ))}
            </div>
        );
    }

function TeamComparison(props) {
    const [comparison, setComparison] = useState({});
    const [isLoading, setIsLoading] = useState(true);

        useEffect(() => {
        const compareTeams = async () => {
            setIsLoading(true);
            await axios.get(`http://localhost:5000/team/compare?team1=${props.team1.team}&team2=${props.team2.team}`)
                .then(response => {setComparison(response.data.Comparison); console.log(response.data); })
                .catch(() => {});
            setIsLoading(false);
        };

            compareTeams();
    },[])

    if (isLoading){
        return (
            <Container align="center">
                <h1>Loading...</h1>
                <Spinner animation="border"/>
            </Container>
        )
    } else {
        let averages = [
            {name:'Goal Allowed', team1: comparison.average_stats_team1.goals_allowed, team2: comparison.average_stats_team2.goals_allowed}, 
            {name:'Goals for', team1: comparison.average_stats_team1.goals_for, team2: comparison.average_stats_team2.goals_for}, 
            {name: 'Shots', team1: comparison.average_stats_team1.shots, team2: comparison.average_stats_team2.shots},
            {name: 'Shots on goal',team1: comparison.average_stats_team1.shots_on_goal, team2: comparison.average_stats_team2.shots_on_goal},
            {name: 'Saves', team1: comparison.average_stats_team1.saves, team2:  comparison.average_stats_team2.saves},
            {name: 'Passes', team1: comparison.average_stats_team1.passes, team2: comparison.average_stats_team2.passes},
            {name: 'Possessions', team1: comparison.average_stats_team1.possession, team2: comparison.average_stats_team2.possession},
            {name: 'Fouls', team1: comparison.average_stats_team1.fouls, team2: comparison.average_stats_team2.fouls},
        ];

        const most_favored = (comparison.most_favored === "team1") ? props.team1.team_name : props.team2.team_name; 

        return (
            <Container align="center">
                <h1>{props.team1.team_name} VS {props.team2.team_name}</h1>
                <div style={{ width: '100%', height: 300}}>
                    <ResponsiveContainer>
                    <BarChart
                        data={averages}
                        margin={{
                        top: 5, right: 30, left: 20, bottom: 5,
                        }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="team1" fill="#8884d8" />
                        <Bar dataKey="team2" fill="#82ca9d" />
                    </BarChart>
                    </ResponsiveContainer>
                </div>
                <h2>Team that will most likely win: {most_favored}</h2>
            </Container>
        );
    }
}

function TeamCompare(props) {
    const [teamToCompare, setTeamToCompare] = useState();
    const isInitialMount = useRef(true);

   if (teamToCompare) {
       return <TeamComparison team1={props.team} team2={teamToCompare}/>
   } else {
       return <TeamChooser setTeamToCompare={setTeamToCompare}/>
   }
}

export default TeamCompare
