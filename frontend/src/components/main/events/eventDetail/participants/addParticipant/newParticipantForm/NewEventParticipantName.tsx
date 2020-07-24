/**
 * Provides name for a new participant
 */

import React from "react";

import useStyles from "./styles";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";

interface NameFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  eventName: string;
  error: boolean;
}

/**
 * Text field. Provides name for new participant
 */
function NameField(props: NameFieldProps) {
  const classes = useStyles();

  return (
    <Grid className={classes.textGrid} item xs={12}>
      <TextField
        className={classes.textField}
        required
        error={props.error}
        id="outlined-required-email"
        label="participant name"
        value={props.eventName}
        variant="outlined"
        fullWidth
        onChange={props.handleChange}
      />
    </Grid>
  );
}

export default NameField;
