/**
 * Cell with an amount share of the participant
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

interface AmountCellProps {
  amount: number;
  currency: string;
}

function AmountCell(props: AmountCellProps) {
  return (
    <TableCell>
      {props.amount.toFixed(2)}&nbsp;{props.currency}
    </TableCell>
  );
}

export default AmountCell;
