/**
 * Cell with name of the bill's payer
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";
import Select from "@material-ui/core/Select";
import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import {
  ParticipantInterface,
  BillInterface
} from "../../../../../../../../interfaces/interfaces";
import MenuItem from "@material-ui/core/MenuItem";

import billsService from "../../../../../../../../services/bills";
import useStyles from "../../../styles";

interface PayerCellProps {
  payerId: number;
  eventParticipants: ParticipantInterface[];
  bill: BillInterface;
}

/**
 * Shows bill's current payer. Payer can be changed when user points this cell.
 */
function PayerCell(props: PayerCellProps) {
  const classes = useStyles();
  const [payerId, setPayerId] = React.useState(props.payerId);

  const handleChange = (event: React.ChangeEvent<{ value: unknown }>) => {
    setPayerId(event.target.value as number);
    let oldBillData = props.bill;

    oldBillData.payer = event.target.value as number;
    billsService.updateBill(props.bill.url, oldBillData).subscribe();
  };

  return payerId && props.eventParticipants ? (
    <TableCell align="right">
      <FormControl className={classes.changePayerForm}>
        <InputLabel id="payer-label">Payer</InputLabel>
        <Select
          labelId="payer-label"
          id="payer"
          value={payerId}
          onChange={handleChange}
        >
          {props.eventParticipants.map(participant => (
            <MenuItem value={participant.id} key={participant.id}>
              {participant.username}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </TableCell>
  ) : null;
}

export default PayerCell;
