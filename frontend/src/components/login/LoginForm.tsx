/**
 * FOrm for email and password to log in
 */

import React, { Fragment } from "react"

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Grid, TextField } from "@material-ui/core";


const useStyles = makeStyles(() =>
  createStyles({
    textFieldGrid: {
      paddingTop: "3%"
    },
    textField: {
      width: "85%",
    }
  }),
);

function LoginForm() {

  const classes = useStyles()

  return (
    <Fragment>
      <Grid
        item
        xs={12}
        className={classes.textFieldGrid}
      >
        <TextField
          className={classes.textField}
          required
          id="outlined-required"
          label="email"
          placeholder="example@email.com"
          variant="outlined"
          fullWidth
        />
      </Grid>
      <Grid
        item
        xs={12}
        className={classes.textFieldGrid}
      >
        <TextField
          className={classes.textField}
          required
          type="password"
          id="outlined-required"
          label="password"
          placeholder="example@email.com"
          variant="outlined"
          fullWidth
        />
      </Grid>
    </Fragment>
  );
}

export default LoginForm
