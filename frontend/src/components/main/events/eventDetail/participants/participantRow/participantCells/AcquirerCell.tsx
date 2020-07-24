/**
 * Cell in table with amount of the participant's payments, where participant is an acquirer
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

import { PaymentInterface } from "../../../../../../../interfaces/interfaces";
import { countPaymentsAcquirer } from "../../utils";

interface AcquirerCellInterface {
  payments: PaymentInterface[];
  participantId: number;
}

function AcquirerCell(props: AcquirerCellInterface) {
  return (
    <TableCell align="right">
      {countPaymentsAcquirer(props.payments, props.participantId)}
    </TableCell>
  );
}

export default AcquirerCell;
