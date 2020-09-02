/**
 * Table with name of the participant and his or her share of the bill
 */
import React from "react";

import AddCircleOutlineIcon from "@material-ui/icons/AddCircleOutline";
import Button from "@material-ui/core/Button";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";

import {
  BillInterface,
  ParticipantInterface
} from "../../../../../../../../../interfaces/interfaces";
import NameRow from "./namesRow/NamesRow";
import SelectParticipant from "./selectParticipants/SelectParticipants";

interface NamesTableProps {
  bill: BillInterface;
  eventId: number;
  eventParticipants: ParticipantInterface[];
}

function NamesTable(props: NamesTableProps) {
  const [open, setOpen] = React.useState(false);

  const handleOpen = () => {
    setOpen(!open);
  };

  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell>
            <b>Name</b>
          </TableCell>
          <TableCell>
            <b>Amount</b>
          </TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {props.bill.participants.map(participantId => (
          <NameRow
            participantId={participantId}
            eventId={props.eventId}
            amount={
              parseFloat(props.bill.amount) / props.bill.participants.length
            }
            currency={props.bill.amount_currency}
            billUrl={props.bill.url}
            key={participantId}
          />
        ))}
        <TableRow>
          <TableCell colSpan={2} align="left">
            <Button
              size="small"
              variant="contained"
              color="primary"
              startIcon={<AddCircleOutlineIcon />}
              onClick={handleOpen}
            >
              Choose participants
            </Button>
            <SelectParticipant
              bill={props.bill}
              open={open}
              handleOpen={handleOpen}
              eventParticipants={props.eventParticipants}
              includedParticipants={props.bill.participants}
            />
          </TableCell>
        </TableRow>
      </TableBody>
    </Table>
  );
}

export default NamesTable;
