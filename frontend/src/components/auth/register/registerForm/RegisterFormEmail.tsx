/**
 * Field for email to register
 */

import React from "react";

import { Grid, TextField } from "@material-ui/core";

import useStyles from "./styles";

interface EmailFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  email: string;
  error: string;
}

/**
 * Text field for email
 */
function EmailField(props: EmailFieldProps) {
  const classes = useStyles();

  return (
    <Grid item xs={12} className={classes.textFieldGrid}>
      <TextField
        className={classes.textField}
        required
        error={!!props.error}
        helperText={props.error}
        id="outlined-required-email"
        label="email"
        value={props.email}
        placeholder="example@email.com"
        variant="outlined"
        fullWidth
        onChange={props.handleChange}
      />
    </Grid>
  );
}

export default EmailField;
