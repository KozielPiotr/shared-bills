/**
 * Form for email, password and repeated password to register new user
 */

import React from "react";

import { Button } from "@material-ui/core";

import useObservable from "../../../../hooks/observable";
import authService from "../../../../services/auth";
import useStyles from "./styles";
import RegisterError from "./RegisterError";
import RegisterSuccess from "./RegisterSuccess";
import EmailField from "./RegisterFormEmail";
import PasswordField from "./RegisterFormPassword";

interface RegisterState {
  email: string;
  password: string;
  password2: string;
}

/**
 * Form with email, password and repeated password
 */
function RegisterForm() {
  const registerInitialState = {
    email: "",
    password: "",
    password2: ""
  };

  const [registerData, setRegisterData] = React.useState<RegisterState>(
    registerInitialState
  );
  const [registerErrors, setRegisterErrors] = React.useState<RegisterState>(
    registerInitialState
  );
  const [error, setError] = React.useState();
  const registeredUser = useObservable(authService.justRegistered());

  React.useEffect(() => {
    setRegisterErrors({
      email: validateEmail(),
      password: validatePassword(),
      password2: validatePassword2()
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [registerData]);

  /**
   * Checks if email is in proper format
   */
  const validateEmail = () => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return !registerData.email ||
      re.test(String(registerData.email).toLowerCase())
      ? ""
      : "Wrong email format.";
  };

  /**
   * Checks if password has proper length
   */
  const validatePassword = () =>
    !registerData.password || registerData.password.length >= 8
      ? ""
      : "Password must be at least 8 characters long.";

  /**
   * Checks if passwords are identical
   */
  const validatePassword2 = () =>
    !registerData.password ||
    !registerData.password2 ||
    registerData.password === registerData.password2
      ? ""
      : "Passwords must be identical.";

  const handleChange = (field: keyof RegisterState) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setRegisterData({ ...registerData, [field]: event.target.value });
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
        errors={[registerErrors.password]}
        placeholder="password"
        label="password"
      />
      <PasswordField
        id="password2"
        handleChange={handleChange("password2")}
        password={registerData.password2}
        errors={[registerErrors.password2]}
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
          !!registerErrors.password2
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
