/**
 * Main application
 */

import React from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";

import MainPage from "./main/Main";
import RegisterPage from "./register/Register";

/**
 * Main application function
 */
function App() {
  return (
    <Router>
      <Route exact path="/" component={MainPage} />
      <Route exact path="/register" component={RegisterPage} />
    </Router>
  );
}

export default App;
