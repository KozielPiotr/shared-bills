/**
 * Main page
 */

import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";

import authService from "../../services/auth";
import useStyles from "./styles";
import Events from "./events/Events";
import EventDetail from "./events/eventDetail/EventDetail";

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
      <Router>
        <div className={classes.content}>
          <Route exact path="/" component={Events} />
          <Route path="/event/:id" component={EventDetail} />
        </div>
      </Router>
    </div>
  );
}

export default MainPage;
