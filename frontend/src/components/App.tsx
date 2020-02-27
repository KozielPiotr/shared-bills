/**
 * Main application
 */

import React from "react";

import authService from "../services/auth";

import MainPage from "./main/Main";
import LoginPage from "./login/Login";

/**
 * Main application function
 */
function App() {
  const [isAuthenticated, setAuthenticated] = React.useState<boolean>(false);

  React.useEffect(() => {
    const subscription = authService
      .isAuthenticated()
      .subscribe(setAuthenticated);
    return () => subscription.unsubscribe();
  }, []);

  return isAuthenticated ? <MainPage /> : <LoginPage />;
}

export default App;
