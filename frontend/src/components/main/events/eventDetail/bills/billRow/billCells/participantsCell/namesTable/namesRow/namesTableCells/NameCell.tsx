/**
 * Cell with a name of the participant
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

interface NameCellProps {
  participant: string;
}

function NameCell(props: NameCellProps) {
  return <TableCell>{props.participant}</TableCell>;
}

export default NameCell;
