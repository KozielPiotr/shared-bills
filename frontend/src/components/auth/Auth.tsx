/**
 * Component to manage login/authorisation process
 */

import React from "react";

import authService from "../../services/auth";
import useObservable from "../../hooks/observable";

import LoginPage from "./login/Login";
import RegisterPage from "./register/Register";

/**
 * Renders login or registration page
 */
function AuthPage() {
  const login = useObservable(authService.loginOrRegister());

  return login ? <LoginPage /> : <RegisterPage />;
}

export default AuthPage;
