/**
 * Cell in table with an amount of the bill
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

interface AmountCellProps {
  amount: string;
  currency: string;
}

function AmountCell(props: AmountCellProps) {
  return (
    <TableCell align="right">
      <b>{parseFloat(props.amount).toFixed(2)}</b>&nbsp;{props.currency}
    </TableCell>
  );
}

export default AmountCell;
