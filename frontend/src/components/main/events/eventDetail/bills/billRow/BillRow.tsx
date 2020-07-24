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
import PayerCell from "./billCells/PayerCell";

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
  const payer = useObservable(participantService.participant$);
  const participants = useObservable(participantService.participants$);

  React.useEffect(() => {
    participantService.fetchParticipantById(props.eventId, props.payerId);
    participantService.fetchParticipants(props.participantsUrl);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return payer ? (
    <TableRow>
      <TitleCell billTitle={props.billTitle} />
      <AmountCell amount={props.amount} currency={props.currency} />
      <ParticipantsCell
        billUrl={props.billUrl}
        eventId={props.eventId}
        eventParticipants={participants}
      />
      <PayerCell payerName={payer.username} />
    </TableRow>
  ) : null;
}

export default BillRow;
