/**
 * Form for email and password to log in
 */

import React from "react";

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Button } from "@material-ui/core";

import EmailField from "./LoginFormEmail";
import PasswordField from "./LoginFormPassword";

import authService from "../../../services/auth";

const useStyles = makeStyles(() =>
  createStyles({
    button: {
      marginTop: "3%",
      width: "85%"
    }
  })
);

interface State {
  email: string;
  password: string;
}

/**
 * Form with user email and password
 */
function LoginForm() {
  const classes = useStyles();

  const [authData, setAuthData] = React.useState<State>({
    email: "",
    password: ""
  });

  const handleChange = (prop: keyof State) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setAuthData({ ...authData, [prop]: event.target.value });
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    authService.login(authData).subscribe({ error: error => alert(error) });
  };

  return (
    <form onSubmit={handleSubmit}>
      <EmailField handleChange={handleChange("email")} email={authData.email} />
      <PasswordField
        handleChange={handleChange("password")}
        password={authData.password}
      />
      <Button
        type="submit"
        className={classes.button}
        variant="contained"
        color="primary"
      >
        Log in
      </Button>
    </form>
  );
}

export default LoginForm;
