/**
 * Main application
 */

import React from "react";

import authService from "../services/auth";
import useObservable from "../hooks/observable";

import MainPage from "./main/Main";
import LoginPage from "./login/Login";

/**
 * Main application function
 */
function App() {
  const isAuthenticated = useObservable(authService.isAuthenticated());

  return isAuthenticated ? <MainPage /> : <LoginPage />;
}

export default App;
