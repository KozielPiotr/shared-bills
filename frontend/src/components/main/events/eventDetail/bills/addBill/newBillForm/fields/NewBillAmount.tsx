/**
 * Provides an amount for the new bill
 */

import React from "react";

import useStyles from "../styles";
import TextField from "@material-ui/core/TextField";

interface AmountFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  error: boolean;
}

function AmountField(props: AmountFieldProps) {
  const classes = useStyles();

  return (
    <TextField
      className={classes.textField}
      required
      error={props.error}
      id="outlined-required-email"
      label="amount"
      variant="outlined"
      helperText={
        props.error ? "Only decimals. Can be separated by a dot." : ""
      }
      fullWidth
      onChange={props.handleChange}
    />
  );
}

export default AmountField;
