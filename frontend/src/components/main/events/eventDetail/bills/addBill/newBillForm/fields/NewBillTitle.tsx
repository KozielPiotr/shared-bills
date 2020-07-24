/**
 * Provides a title for the new bill
 */

import React from "react";

import useStyles from "../styles";
import Grid from "@material-ui/core/Grid";
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
    <Grid className={classes.textGrid} item xs={6}>
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
    </Grid>
  );
}

export default TitleField;