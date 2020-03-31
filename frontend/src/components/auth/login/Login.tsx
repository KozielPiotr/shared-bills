/**
 * Login page
 */

import React from "react";

import { Button, Grid, Paper, Typography } from "@material-ui/core";

import authService, { AuthStage } from "../../../services/auth";
import useStyles from "./styles";
import LoginForm from "./loginForm/LoginForm";

/**
 * Main component for login page
 */
function LoginPage() {
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
              Welcome to Shared-bills app!
            </Typography>
          </Grid>
          <LoginForm />
          <Typography
            variant="subtitle2"
            gutterBottom
            className={classes.typography}
          >
            Don't have an account?
            <Button
              onClick={() => authService.setAuthAction(AuthStage.Register)}
              color="primary"
            >
              Create one!
            </Button>
          </Typography>
        </Paper>
      </Grid>
    </Grid>
  );
}

export default LoginPage;
