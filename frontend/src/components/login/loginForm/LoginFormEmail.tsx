/**
 * Field for email to log in
 */

import React from "react";

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Grid, TextField } from "@material-ui/core";

import { EmailFieldProps } from "./utils/interfaces";

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
 * Text field for email
 */
function EmailField(props: EmailFieldProps) {
  const classes = useStyles();

  return (
    <Grid item xs={12} className={classes.textFieldGrid}>
      <TextField
        className={classes.textField}
        required
        error={props.error}
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
