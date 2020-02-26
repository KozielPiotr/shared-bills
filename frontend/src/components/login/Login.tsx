/**
 * Login page
 */

import React from "react"

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Grid, Paper, Typography } from "@material-ui/core";

import LoginForm from "./LoginForm"

const useStyles = makeStyles(() =>
  createStyles({
    grid: {
      textAlign: "center",
      justifyContent: "center",
      alignContent: "center",
      flexWrap: "nowrap",
      backgroundColor: "#f5f5f5",
      paddingLeft: "15%",
      paddingRight: "15%",
    },
    paper: {
      margin: 0,
      paddingTop: "3%",
      paddingBottom: "3%",
      marginLeft: "25%",
      marginRight: "25%",
    },
    typography: {
      padding: "1%",
      textAlign: "center",
    },
    welcome: {
      textAlign: "center",
    },
    textFieldGrid: {
      paddingTop: "3%"
    },
    textField: {
      width: "85%",
    }
  }),
);

/**
 * Main component for login page
 */
function LoginPage() {
  
  const classes = useStyles();

  return (
    <Grid
      container
      className={classes.grid}
      spacing={0}
      direction="column"
    >
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
        </Paper>
      </Grid>
    </Grid>
  );
}

export default LoginPage
