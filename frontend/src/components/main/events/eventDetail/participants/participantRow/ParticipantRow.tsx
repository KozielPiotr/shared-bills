/**
 * Table row with info about the participant
 */

import React from "react";

import TableRow from "@material-ui/core/TableRow";

import {
  ParticipantInterface,
  BillInterface,
  PaymentInterface
} from "../../../../../../interfaces/interfaces";
import NameCell from "./participantCells/NameCell";
import BillsCell from "./participantCells/BillsCell";
import AcquirerCell from "./participantCells/AcquirerCell";
import IssuerCell from "./participantCells/IssuerCell";

interface ParticipantRowInterface {
  participant: ParticipantInterface;
  paymasterId: number;
  bills: BillInterface[];
  payments: PaymentInterface[];
  handleOpenDelete: (participantUrl: string) => void;
  key: number;
}

/**
 * Component with detailed info about the participant
 */

function ParticipantRow(props: ParticipantRowInterface) {
  return (
    <TableRow>
      <NameCell
        participantId={props.participant.id}
        paymasterId={props.paymasterId}
        participantName={props.participant.username}
        participantUrl={props.participant.url}
        handleOpenDelete={props.handleOpenDelete}
      />
      <BillsCell
        bills={props.bills}
        participantId={props.participant.id}
      ></BillsCell>
      <AcquirerCell
        payments={props.payments}
        participantId={props.participant.id}
      />
      <IssuerCell
        payments={props.payments}
        participantId={props.participant.id}
      />
    </TableRow>
  );
}

export default ParticipantRow;
