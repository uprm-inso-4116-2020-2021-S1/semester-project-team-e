import React, { Component } from 'react';
import Header from "../Components/header";
import BootstrapTable from "react-bootstrap-table-next";


class ListSport extends Component {

    state = {
        loading: false,
        sports: [{
            text: 'Soccer'
        },
        {
            text: 'Basketball'
        }],
        columns: [{
            dataField: 'text',
            text: 'Sport'
        }]
    };

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
                            Sports
                        </div>
                    </div>
                    <div style={{marginTop: 20, backgroundColor: "white"}}>
                        <BootstrapTable bordered striped hover variant="dark" keyField='team_id'
                                        data={this.state.sports} columns={this.state.columns}></BootstrapTable>
                    </div>
                </div>
            </div>
        )
    }
}
export default ListSport;