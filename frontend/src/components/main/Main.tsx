/**
 * Main page
 */

import React from "react";

import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

import authService from "../../services/auth";
import Events from "./events/Events";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    root: {
      flexGrow: 1
    },
    title: {
      flexGrow: 1,
      textAlign: "center"
    }
  })
);

/**
 * Main component for main page
 */
function MainPage() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Shared Bills
          </Typography>
          <Button color="inherit" onClick={authService.logout}>
            Logout
          </Button>
        </Toolbar>
      </AppBar>
      <Events />
    </div>
  );
}

export default MainPage;
