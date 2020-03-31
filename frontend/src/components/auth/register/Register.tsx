/**
 * Registration page
 */

import React from "react";

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Button, Grid, Paper, Typography } from "@material-ui/core";

import authService, { AuthStage } from "../../../services/auth";

import RegisterForm from "./registerForm/RegisterForm";

const useStyles = makeStyles(() =>
  createStyles({
    grid: {
      textAlign: "center",
      justifyContent: "center",
      alignContent: "center",
      flexWrap: "nowrap",
      paddingLeft: "15%",
      paddingRight: "15%"
    },
    paper: {
      margin: 0,
      paddingTop: "3%",
      paddingBottom: "3%",
      marginLeft: "25%",
      marginRight: "25%"
    },
    typography: {
      padding: "1%",
      textAlign: "center"
    }
  })
);

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
