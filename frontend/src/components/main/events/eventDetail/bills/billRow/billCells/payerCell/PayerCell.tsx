/**
 * Cell with name of the bill's payer
 */

import React from "react";

import TableCell from "@material-ui/core/TableCell";
import Select from "@material-ui/core/Select";
import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import { ParticipantInterface } from "../../../../../../../../interfaces/interfaces";
import MenuItem from "@material-ui/core/MenuItem";

import BillsService from "../../../../../../../../services/bills";
import useObservable from "../../../../../../../../hooks/observable";
import useStyles from "../../../styles";

interface PayerCellProps {
  payer: ParticipantInterface;
  eventParticipants: ParticipantInterface[];
  billUrl: string;
}

/**
 * Shows bill's current payer. Payer can be changed when user points this cell.
 */
function PayerCell(props: PayerCellProps) {
  const classes = useStyles();
  const [payer, setPayer] = React.useState(props.payer.id);
  const billData = useObservable(BillsService.bill$);

  const handleChange = (event: React.ChangeEvent<{ value: unknown }>) => {
    setPayer(event.target.value as number);
    let oldBillData = billData;
    oldBillData.payer = event.target.value;
    BillsService.updateBill(props.billUrl, oldBillData).subscribe();
  };

  return (
    <TableCell align="right">
      <FormControl className={classes.changePayerForm}>
        <InputLabel id="payer-label">Payer</InputLabel>
        <Select
          labelId="payer-label"
          id="payer"
          value={payer}
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
  );
}

export default PayerCell;
