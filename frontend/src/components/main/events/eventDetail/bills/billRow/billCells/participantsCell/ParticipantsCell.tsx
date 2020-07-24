/**
 * Cell with number of the bill's participants.
 */

import React from "react";

import { BehaviorSubject } from "rxjs";
import { map } from "rxjs/operators";

import IconButton from "@material-ui/core/IconButton";
import KeyboardArrowDownIcon from "@material-ui/icons/KeyboardArrowDown";
import KeyboardArrowUpIcon from "@material-ui/icons/KeyboardArrowUp";
import TableCell from "@material-ui/core/TableCell";

import {
  BillInterface,
  ParticipantInterface
} from "../../../../../../../../interfaces/interfaces";
import { ApiServiceExact } from "../../../../../../../../services/api";
import useObservable from "../../../../../../../../hooks/observable";
import NamesTable from "./namesTable/NamesTable";

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
  const bill$ = new BehaviorSubject<BillInterface[]>([]);
  const bill = useObservable(bill$);

  const openParticipantsList = () => {
    setOpen(!open);
  };

  const apiServiceExact = new ApiServiceExact();

  const fetchBill = () => {
    apiServiceExact
      .get(props.billUrl)
      .pipe(map(ajax => ajax.response))
      .subscribe(bill => {
        bill$.next(bill);
      });
  };

  React.useEffect(() => {
    fetchBill();
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
          fetchBill={fetchBill}
          eventParticipants={props.eventParticipants}
        />
      ) : null}
    </TableCell>
  ) : null;
}

export default ParticipantsCell;
