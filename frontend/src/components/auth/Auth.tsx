/**
 * Component to manage login/authorisation process
 */

import React from "react";

import authService, { AuthStage } from "../../services/auth";
import useObservable from "../../hooks/observable";

import LoginPage from "./login/Login";
import RegisterPage from "./register/Register";

/**
 * Renders login or registration page
 */
function AuthPage() {
  const authDecision = useObservable(authService.authAction());

  // if (authDecision === AuthStage.Login) {
  //   return <LoginPage />;
  // } else if (authDecision === AuthStage.Register) {
  //   return <RegisterPage />;
  // } else {
  //   return <LoginPage />;
  // }

  switch (authDecision) {
    case AuthStage.Login:
      return <LoginPage />;
    case AuthStage.Register:
      return <RegisterPage />;
    default:
      return <LoginPage />;
  }
}

export default AuthPage;
