/**
 * Cell with name of the bill's payer
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

interface PayerCellProps {
  payerName: string;
}

function PayerCell(props: PayerCellProps) {
  return <TableCell align="right">{props.payerName}</TableCell>;
}

export default PayerCell;
