/**
 * Cell in table with name of the participant
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";
import IconButton from "@material-ui/core/IconButton";
import DeleteForeverIcon from "@material-ui/icons/DeleteForever";

interface NameCellProps {
  participantId: number;
  paymasterId: number;
  participantName: string;
  participantUrl: string;
  handleOpenDelete: (participantUrl: string) => void;
}

function NameCell(props: NameCellProps) {
  const handleClick = () => {
    props.handleOpenDelete(props.participantUrl);
  };

  return (
    <TableCell component="th" scope="row">
      <IconButton onClick={handleClick}>
        <DeleteForeverIcon color="secondary" />
      </IconButton>
      {props.participantId === props.paymasterId ? (
        <b>{props.participantName} (paymaster)</b>
      ) : (
        props.participantName
      )}
    </TableCell>
  );
}
export default NameCell;
