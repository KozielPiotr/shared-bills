import React, { Fragment } from "react";
import {
	BrowserRouter as Router,
	Route,
} from "react-router-dom"

import MainPage from "./main/Main"
import LoginPage from "./login/Login"


/**
 * Main application function
 */
function App() {

  return (
    <Fragment>
    <Router>
			<Route exact path="/" component={MainPage} />
      <Route exact path="/login" component={LoginPage} />
		</Router>
    </Fragment>
  );
}

export default App;
