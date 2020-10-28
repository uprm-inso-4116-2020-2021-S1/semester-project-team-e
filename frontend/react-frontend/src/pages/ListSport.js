import React, { Component } from 'react';
import Table from '../Components/TableComponent'
import schemaSports from '../Components/schemaSports.json';
import data from '../Components/data.json'
import {Col, Row} from "reactstrap";
import Header from "../Components/header";

class ListSport extends Component {
    render() {
        const styles = {
            container:{
                height: '500px',
                width: '1200px'
            },
            table:{
                height: '700px',
                width: '1200px',
                margin_left: 'auto',
                position: 'absolute',
                top: '150px',
                right: '300px',
                left: '310px'
            }
          }
        return<div className="container p-2" >
            <Header/>
      <div className="row">
        <div className="col" style = {styles.table}>
          <Table headers={Object.keys(schemaSports)} rows={data} />
        </div>
      </div>
    </div>
    }
}
export default ListSport;