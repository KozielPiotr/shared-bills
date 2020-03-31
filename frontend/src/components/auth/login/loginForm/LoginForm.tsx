/**
 * Form for email and password to log in
 */

import React from "react";

import { Button, Typography } from "@material-ui/core";

import authService from "../../../../services/auth";
import useStyles from "./styles";
import EmailField from "./LoginFormEmail";
import PasswordField from "./LoginFormPassword";

interface AuthState {
  email: string;
  password: string;
}

/**
 * Form with user email and password
 */
function LoginForm() {
  const classes = useStyles();

  const [authData, setAuthData] = React.useState<AuthState>({
    email: "",
    password: ""
  });

  const [error, setError] = React.useState(false);

  const handleChange = (prop: keyof AuthState) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setAuthData({ ...authData, [prop]: event.target.value });
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    authService
      .login(authData)
      .subscribe({ error: error => setError(error ? true : false) });
  };

  return (
    <form onSubmit={handleSubmit}>
      {error ? (
        <Typography variant="subtitle2" color="error" gutterBottom>
          Wrong email or password. Please try again.
        </Typography>
      ) : null}
      <EmailField
        handleChange={handleChange("email")}
        email={authData.email}
        error={error}
      />
      <PasswordField
        handleChange={handleChange("password")}
        password={authData.password}
        error={error}
      />
      <Button
        type="submit"
        className={classes.button}
        disabled={!authData.email || !authData.password}
        variant="contained"
        color="primary"
      >
        Log in
      </Button>
    </form>
  );
}

export default LoginForm;
