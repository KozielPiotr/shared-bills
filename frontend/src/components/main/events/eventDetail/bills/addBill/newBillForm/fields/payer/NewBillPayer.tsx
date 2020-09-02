/**
 * Select field with all event's participants. User can choose bill's paymaster.
 * Paymaster doesn't have to be assigned to the bill as it's participant.
 */

import React, { Fragment } from "react";

import FormControl from "@material-ui/core/FormControl";
import InputLabel from "@material-ui/core/InputLabel";
import Select from "@material-ui/core/Select";
import MenuItem from "@material-ui/core/MenuItem";

import { ParticipantInterface } from "../../../../../../../../../interfaces/interfaces";

interface PaymasterFieldProps {
  participants: ParticipantInterface[];
  paymaster: number;
  handleChangePayer: (payerId: number) => void;
}

/**
 * Bill's paymaster choice
 */
function PaymasterField(props: PaymasterFieldProps) {
  const handleChange = (event: React.ChangeEvent<{ value: unknown }>) => {
    props.handleChangePayer(event.target.value as number);
  };
  return (
    <Fragment>
      <FormControl variant="outlined" fullWidth required>
        <InputLabel id="paymaster-select">paymaster</InputLabel>
        <Select
          labelId="paymaster-select"
          id="paymaster-select"
          value={props.paymaster}
          onChange={handleChange}
          label="Age"
        >
          {props.participants.map(participant => (
            <MenuItem key={participant.id} value={participant.id}>
              {participant.username}
            </MenuItem>
          ))}
        </Select>
      </FormControl>
    </Fragment>
  );
}

export default PaymasterField;
