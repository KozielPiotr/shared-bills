/**
 * Field for password to log in
 */

import React from "react";

import { Grid, TextField } from "@material-ui/core";

import useStyles from "./styles";

interface PasswordFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  password: string;
  error: boolean;
}

/**
 * Text field for password
 */
function PasswordField(props: PasswordFieldProps) {
  const classes = useStyles();

  return (
    <Grid item xs={12} className={classes.textFieldGrid}>
      <TextField
        className={classes.textField}
        required
        type="password"
        error={props.error}
        id="outlined-required-password"
        label="password"
        value={props.password}
        placeholder="password"
        variant="outlined"
        fullWidth
        onChange={props.handleChange}
      />
    </Grid>
  );
}

export default PasswordField;
