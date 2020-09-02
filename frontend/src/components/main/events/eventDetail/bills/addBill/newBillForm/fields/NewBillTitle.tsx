/**
 * Provides a title for the new bill
 */

import React from "react";

import useStyles from "../styles";
import TextField from "@material-ui/core/TextField";

interface TitleFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  error: boolean;
}

/**
 * Text field. Provides title for new bill
 */
function TitleField(props: TitleFieldProps) {
  const classes = useStyles();

  return (
    <TextField
      className={classes.textField}
      required
      error={props.error}
      id="outlined-required-email"
      label="title"
      variant="outlined"
      fullWidth
      onChange={props.handleChange}
    />
  );
}

export default TitleField;
