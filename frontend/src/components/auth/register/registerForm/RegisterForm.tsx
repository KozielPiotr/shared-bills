/**
 * Form for email, password and repeated password to register new user
 */

import React from "react";

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Button } from "@material-ui/core";

import useObservable from "../../../../hooks/observable";
import RegisterError from "./RegisterError";
import RegisterSuccess from "./RegisterSuccess";
import EmailField from "./RegisterFormEmail";
import PasswordField from "./RegisterFormPassword";

import authService from "../../../../services/auth";

const useStyles = makeStyles(() =>
  createStyles({
    button: {
      marginTop: "3%",
      width: "85%"
    }
  })
);

interface RegisterState {
  email: string;
  password: string;
  password2: string;
  passwordsComparison: string;
}

/**
 * Form with email, password and repeated password
 */
function RegisterForm() {
  const registerInitialState = {
    email: "",
    password: "",
    password2: "",
    passwordsComparison: ""
  };

  const [registerData, setRegisterData] = React.useState<RegisterState>(
    registerInitialState
  );
  const [registerErrors, setRegisterErrors] = React.useState<RegisterState>(
    registerInitialState
  );
  const [error, setError] = React.useState();
  const registeredUser = useObservable(authService.justRegistered());

  /**
   * Checks if email has correct format
   *
   * @param { string } input Email entered by user
   */
  const validateEmail = (input: string) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(input).toLowerCase()) ? "" : "Wrong email format.";
  };

  /**
   * Checks if password has correct length and if repeated password is identical as password
   *
   * @param { string } input Password entered by user
   */
  const validatePassword = (input: string) => {
    if (input.length >= 8) return "";
    else {
      console.log("too short");
      return "Password must be at least 8 characters long.";
    }
  };

  /**
   * Checks if repeated password is identical as password
   *
   * @param { string} field password or repeated password input field
   * @param { string } input Password entered by user
   */
  const assertPasswords = (field: string, input: string) => {
    if (field === "password") {
      if (input === registerData.password2) return "";
      else return "Passwords must be identical.";
    } else if (field === "password2") {
      if (input === registerData.password) return "";
      else return "Passwords must be identical.";
    } else return "";
  };

  const handleChange = (field: keyof RegisterState) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setRegisterData({ ...registerData, [field]: event.target.value });
    if (field === "email") {
      setRegisterErrors({
        ...registerErrors,
        [field]: validateEmail(event.target.value)
      });
    } else {
      console.log("A", field);
      setRegisterErrors({
        ...registerErrors,
        [field]: validatePassword(event.target.value),
        passwordsComparison: assertPasswords(field, event.target.value)
      });
    }
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    authService
      .register(registerData)
      .subscribe({ error: error => setError(error) });
  };

  const classes = useStyles();

  return (
    <form onSubmit={handleSubmit}>
      {error ? <RegisterError error={error} /> : null}
      {registeredUser !== null ? (
        <RegisterSuccess registeredUser={registeredUser} />
      ) : null}
      <EmailField
        handleChange={handleChange("email")}
        email={registerData.email}
        error={registerErrors.email}
      />
      <PasswordField
        id="password"
        handleChange={handleChange("password")}
        password={registerData.password}
        errors={[registerErrors.password2, registerErrors.passwordsComparison]}
        placeholder="password"
        label="password"
      />
      <PasswordField
        id="password2"
        handleChange={handleChange("password2")}
        password={registerData.password2}
        errors={[registerErrors.password2, registerErrors.passwordsComparison]}
        placeholder="repeat password"
        label="repeat password"
      />
      <Button
        type="submit"
        className={classes.button}
        disabled={
          !registerData.email ||
          !registerData.password ||
          !registerData.password2 ||
          !!registerErrors.email ||
          !!registerErrors.password ||
          !!registerErrors.password2 ||
          !!registerErrors.passwordsComparison
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
