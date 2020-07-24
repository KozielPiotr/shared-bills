/**
 * Cell in table with amount of the participant's payments, where participant is an issuer
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

import { PaymentInterface } from "../../../../../../../interfaces/interfaces";
import { countPaymentsIssuer } from "../../utils";

interface IssuerCellInterface {
  payments: PaymentInterface[];
  participantId: number;
}

function IssuerCell(props: IssuerCellInterface) {
  return (
    <TableCell align="right">
      {countPaymentsIssuer(props.payments, props.participantId)}
    </TableCell>
  );
}

export default IssuerCell;
