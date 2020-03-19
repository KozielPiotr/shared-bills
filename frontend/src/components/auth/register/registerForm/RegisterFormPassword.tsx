/**
 * Field for password to rgister
 */

import React from "react";

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Grid, TextField } from "@material-ui/core";

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

interface PasswordFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  id: string;
  password: string;
  errors: string[];
  placeholder: string;
  label: string;
}

/**
 * Text field for password
 */
function PasswordField(props: PasswordFieldProps) {
  const isError = () => {
    if (props.errors[0] || props.errors[1]) return true;
    else return false;
  };

  const classes = useStyles();
  return (
    <Grid item xs={12} className={classes.textFieldGrid}>
      <TextField
        className={classes.textField}
        required
        type="password"
        error={isError()}
        helperText={props.errors[0] ? props.errors[0] : props.errors[1]}
        id={props.id}
        label={props.label}
        value={props.password}
        placeholder={props.placeholder}
        variant="outlined"
        fullWidth
        onChange={props.handleChange}
      />
    </Grid>
  );
}

export default PasswordField;
