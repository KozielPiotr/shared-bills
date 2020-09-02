/**
 * Cell with number of the bill's participants.
 */

import React from "react";

import IconButton from "@material-ui/core/IconButton";
import KeyboardArrowDownIcon from "@material-ui/icons/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@material-ui/icons/KeyboardArrowUp";
import TableCell from "@material-ui/core/TableCell";

import { ParticipantInterface } from "../../../../../../../../interfaces/interfaces";
import useObservable from "../../../../../../../../hooks/observable";
import NamesTable from "./namesTable/NamesTable";
import BillsService from "../../../../../../../../services/bills";

interface ParticipantsCellProps {
  billUrl: string;
  eventId: number;
  eventParticipants: ParticipantInterface[];
}

/**
 * Cell with number of the bill's participants and expandable table with participant name and share of the bill
 */
function ParticipantsCell(props: ParticipantsCellProps) {
  const [open, setOpen] = React.useState(false);
  const bill = useObservable(BillsService.bill$);

  const openParticipantsList = () => {
    setOpen(!open);
  };

  React.useEffect(() => {
    BillsService.fetchBill(props.billUrl);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return bill && bill.participants ? (
    <TableCell align="right">
      {bill.participants.length}
      <IconButton size="small" onClick={openParticipantsList}>
        {open ? <KeyboardArrowUpIcon /> : <KeyboardArrowDownIcon />}
      </IconButton>
      {open ? (
        <NamesTable
          bill={bill}
          eventId={props.eventId}
          eventParticipants={props.eventParticipants}
        />
      ) : null}
    </TableCell>
  ) : null;
}

export default ParticipantsCell;
