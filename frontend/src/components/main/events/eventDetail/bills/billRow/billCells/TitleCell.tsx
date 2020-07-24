/**
 * Cell in table with a title of the bill
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

interface TitleCellProps {
  billTitle: string;
}

function TitleCell(props: TitleCellProps) {
  return (
    <TableCell component="th" scope="row">
      {props.billTitle}
    </TableCell>
  );
}
export default TitleCell;
