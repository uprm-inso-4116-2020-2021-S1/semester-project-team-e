import React from 'react';

const TableBody = (props) => {
  const { headers, rows } = props;

  function buildRow(row, headers) {
    return (
         <tr key={row}>
         { headers.map((value, index) => {
             return <td key={index}>{row[value]}</td>
          })}
         </tr>
     )
  };

  return(
      <tbody>
        { rows && rows.map((value) => {
                return buildRow(value, headers);
            })}
      </tbody>
);
}

export default TableBody;