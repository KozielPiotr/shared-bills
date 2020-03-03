/**
 * Main page
 */

import React from "react";

import authService from "../../services/auth";
import useObservable from "../../hooks/observable";

import LoginPage from "../login/Login";

/**
 * Main component for main page
 */
function MainPage() {
  const isAuthenticated = useObservable(authService.isAuthenticated());

  return isAuthenticated ? (
    <div>
      <p>
        <button onClick={authService.logout}>Logout</button>
      </p>
    </div>
  ) : (
    <LoginPage />
  );
}

export default MainPage;
