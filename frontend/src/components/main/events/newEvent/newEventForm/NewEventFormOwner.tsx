/**
 * Provides owner for the new event
 */

import React from "react";

import useStyles from "./styles";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";

interface OwnerProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  owner: string;
  error: boolean;
}

/**
 * Text field. Provides name for the new event
 */
function OwnerField(props: OwnerProps) {
  const classes = useStyles();

  return (
    <Grid className={classes.textGrid} item xs={12}>
      <TextField
        className={classes.textField}
        required
        error={props.error}
        id="outlined-required-email"
        label="owner participant"
        value={props.owner}
        variant="outlined"
        fullWidth
        onChange={props.handleChange}
      />
    </Grid>
  );
}

export default OwnerField;
