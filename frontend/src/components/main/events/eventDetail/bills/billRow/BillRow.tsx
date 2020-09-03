/**
 * Row with info about the bill
 */

import React from "react";

import TableRow from "@material-ui/core/TableRow";

import useObservable from "../../../../../../hooks/observable";
import participantService from "../../../../../../services/participants";
import TitleCell from "./billCells/TitleCell";
import AmountCell from "./billCells/AmountCell";
import ParticipantsCell from "./billCells/participantsCell/ParticipantsCell";
import PayerCell from "./billCells/payerCell/PayerCell";
import { BehaviorSubject } from "rxjs";
import { BillInterface } from "../../../../../../interfaces/interfaces";
import billsService from "../../../../../../services/bills";

interface BillRowProps {
  billTitle: string;
  amount: string;
  currency: string;
  eventId: number;
  payerId: number;
  participantsUrl: string;
  billUrl: string;
  key: number;
}

/**
 * Component with detailed info about the bill
 */
function BillRow(props: BillRowProps) {
  const participants = useObservable(participantService.participants$);
  const bill$ = new BehaviorSubject<BillInterface | null>(null);
  const bill = useObservable(bill$);

  React.useEffect(() => {
    participantService.fetchParticipants(props.participantsUrl);
    billsService.fetchBillToObject(props.billUrl, bill$);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <TableRow>
      <TitleCell billTitle={props.billTitle} />
      <AmountCell amount={props.amount} currency={props.currency} />
      <ParticipantsCell
        bill={bill}
        eventId={props.eventId}
        eventParticipants={participants}
      />
      <PayerCell
        payerId={props.payerId}
        eventParticipants={participants}
        bill={bill}
      />
    </TableRow>
  );
}

export default BillRow;
