/**
 * Form for email, password and repeated password to register new user
 */

import React from "react";

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Button } from "@material-ui/core";

import useObservable from "../../../hooks/observable";
import { RegisterState } from "./utils/interfaces";
import RegisterError from "./RegisterError";
import RegisterSuccess from "./RegisterSuccess";
import EmailField from "./RegisterFormEmail";
import PasswordField from "./RegisterFormPassword";

import authService from "../../../services/auth";

const useStyles = makeStyles(() =>
  createStyles({
    button: {
      marginTop: "3%",
      width: "85%"
    }
  })
);

/**
 * Form with email, password and repeated password
 */
function RegisterForm() {
  const classes = useStyles();

  const [registerData, setRegisterData] = React.useState<RegisterState>({
    email: "",
    password: "",
    password2: ""
  });

  const [error, setError] = React.useState(false);
  const registeredUser = useObservable(authService.justRegistered());

  const handleChange = (prop: keyof RegisterState) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setRegisterData({ ...registerData, [prop]: event.target.value });
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    authService
      .register(registerData)
      .subscribe({ error: error => setError(error ? true : false) });
  };

  return (
    <form onSubmit={handleSubmit}>
      {error ? <RegisterError /> : null}
      {registeredUser !== null ? (
        <RegisterSuccess registeredUser={registeredUser} />
      ) : null}
      <EmailField
        handleChange={handleChange("email")}
        email={registerData.email}
        error={error}
      />
      <PasswordField
        id="password"
        handleChange={handleChange("password")}
        password={registerData.password}
        error={error}
      />
      <PasswordField
        id="password2"
        handleChange={handleChange("password2")}
        password={registerData.password2}
        error={error}
      />
      <Button
        type="submit"
        className={classes.button}
        disabled={
          !registerData.email ||
          !registerData.password ||
          !registerData.password2
        }
        variant="contained"
        color="primary"
      >
        Register
      </Button>
    </form>
  );
}

export default RegisterForm;
