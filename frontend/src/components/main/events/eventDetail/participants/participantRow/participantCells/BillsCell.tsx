/**
 * Cell in table with amount of the participant's bills
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";

import { BillInterface } from "../../../../../../../interfaces/interfaces";
import { countBills } from "../../utils";

interface BillsCellInterface {
  bills: BillInterface[];
  participantId: number;
}

function BillsCell(props: BillsCellInterface) {
  return (
    <TableCell align="right">
      {countBills(props.bills, props.participantId)}
    </TableCell>
  );
}

export default BillsCell;
