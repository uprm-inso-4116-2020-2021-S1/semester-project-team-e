import React, { Component } from 'react';
import Table from '../Components/TableComponent'
import schemaPlayers from '../Components/schemaPlayers.json';
import dataPlayers from '../Components/dataPlayers.json';
import {Col, Row} from "reactstrap";
import Header from "../Components/header";
import TeamPreview from '../Components/teampreview';

class ListPlayers extends Component {
  state = {
    loading: true,
    teams : []
  };

  async componentDidMount() {
    const teamUrl = "/team";
    await fetch(teamUrl)
      .then(response => response.json())
      .then(json => this.setState({teams: json.Teams, loading: false}))
  }

  render() {
    if (this.state.loading) {
      return <div className="container p-2">
        <Header/>
        <div class="d-flex justify-content-center">
          <div class="spinner-border text-light" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>
    } 

    return <div  className="container p-2">
      <Header/>
      <div>
        {this.state.teams.map(team => (
          <TeamPreview teamName={team.team_name} teamInfo={team.team_info} sport={team.sport_name}/>
        ))}
      </div>
      </div>
  }

  // render() {
  //     const styles = {
  //         container:{
  //             height: '500px',
  //               width: '1200px'
  //           },
  //           table:{
  //               height: '700px',
  //               width: '1200px',
  //               margin_left: 'auto',
  //               position: 'absolute',
  //               top: '150px',
  //               right: '300px',
  //               left: '310px'
  //           }
  //         }
  //       return<div className="container p-2" >
  //           <Header/>
  //     <div className="row">
  //       <div className="col" style = {styles.table}>
  //         <Table headers={Object.keys(schemaPlayers)} rows={dataPlayers} />
  //       </div>
  //     </div>
  //   </div>
  //   }
}
export default ListPlayers;