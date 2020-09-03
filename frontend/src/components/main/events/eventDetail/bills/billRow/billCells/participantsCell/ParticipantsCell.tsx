/**
 * Cell with number of the bill's participants.
 */

import React from "react";

import IconButton from "@material-ui/core/IconButton";
import KeyboardArrowDownIcon from "@material-ui/icons/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@material-ui/icons/KeyboardArrowUp";
import TableCell from "@material-ui/core/TableCell";

import {
  ParticipantInterface,
  BillInterface
} from "../../../../../../../../interfaces/interfaces";
import NamesTable from "./namesTable/NamesTable";

interface ParticipantsCellProps {
  bill: BillInterface;
  eventId: number;
  eventParticipants: ParticipantInterface[];
}

/**
 * Cell with number of the bill's participants and expandable table with participant name and share of the bill
 */
function ParticipantsCell(props: ParticipantsCellProps) {
  const [open, setOpen] = React.useState(false);

  const openParticipantsList = () => {
    setOpen(!open);
  };

  return props.bill && props.bill.participants ? (
    <TableCell align="right">
      {props.bill.participants.length}
      <IconButton size="small" onClick={openParticipantsList}>
        {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
      </IconButton>
      {open ? (
        <NamesTable
          bill={props.bill}
          eventId={props.eventId}
          eventParticipants={props.eventParticipants}
        />
      ) : null}
    </TableCell>
  ) : null;
}

export default ParticipantsCell;
