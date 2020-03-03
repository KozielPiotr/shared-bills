/**
 * Field for password to rgister
 */

import React from "react";

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Grid, TextField } from "@material-ui/core";

import { PasswordFieldProps } from "./utils/interfaces";

const useStyles = makeStyles(() =>
  createStyles({
    textFieldGrid: {
      paddingTop: "3%"
    },
    textField: {
      width: "85%"
    }
  })
);

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
        id={props.id}
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
