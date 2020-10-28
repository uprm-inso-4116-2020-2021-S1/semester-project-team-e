import React from 'react';
import TableHeader from './TableHeader';
import TableBody from './TableBody';

const Table = (props) => {
  const { headers, rows } = props;
  return (
    <div>
      <table className="table table-striped table-dark">
      <TableHeader headers={headers}></TableHeader>
      <TableBody headers={headers} rows={rows}></TableBody>
      </table>
    </div>
  );
}

export default Table;