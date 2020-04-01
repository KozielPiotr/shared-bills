/**
 * Registration page
 */

import React from "react";

import { Button, Grid, Paper, Typography } from "@material-ui/core";

import authService, { AuthStage } from "../../../services/auth";
import useStyles from "./styles";
import RegisterForm from "./registerForm/RegisterForm";

/**
 * Main component for registration page
 */
function RegisterPage() {
  const classes = useStyles();

  return (
    <Grid container className={classes.grid} spacing={0} direction="column">
      <Grid item>
        <Paper className={classes.paper}>
          <Grid item xs={12}>
            <Typography
              variant="h4"
              gutterBottom
              className={classes.typography}
            >
              Register new user
            </Typography>
          </Grid>
          <RegisterForm />
          <Typography
            variant="subtitle2"
            gutterBottom
            className={classes.typography}
          >
            Already have an account?
            <Button
              onClick={() => authService.setAuthAction(AuthStage.Login)}
              color="primary"
            >
              Log in
            </Button>
          </Typography>
        </Paper>
        <Grid item xs={12}></Grid>
      </Grid>
    </Grid>
  );
}

export default RegisterPage;
