import React, { Component } from 'react';
import Header from "../Components/header";
import BootstrapTable  from "react-bootstrap-table-next";

class ListPlayers extends Component {
  state = {
    loading: true,
    teams : [],
    columns:[{
      dataField: 'team_name',
      text:'Team Name'
    },
    {
      dataField: 'team_info',
      text:'Team Info'
    }
    ]
  };

  async componentDidMount() {
    const teamUrl = "/team";
    await fetch(teamUrl)
      .then(response => response.json())
      .then(json => this.setState({teams: json.Teams, loading: false}))
    console.log(this.state.teams)

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

    return (
      <div className="container p-2">
      <Header/>
      <div>
        <div class="row" className="hdr">
        <div class="col-sm-12 btn btn-info">
          Teams
        </div>
          </div>
        <div  style={{ marginTop: 20, backgroundColor:"white"}}>
          <BootstrapTable  bordered striped hover variant="dark" keyField='team_id' data = {this.state.teams} columns = {this.state.columns}></BootstrapTable >
        </div>
        </div>
      </div>
    )
  }
}
export default ListPlayers;