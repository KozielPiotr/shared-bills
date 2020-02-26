/**
 * Form for email and password to log in
 */

import React, { Fragment } from "react"

import { createStyles, makeStyles } from "@material-ui/core/styles";
import { Button } from "@material-ui/core";

import EmailField from "./LoginFormEmail"
import PasswordField from "./LoginFormPassword"


const useStyles = makeStyles(() =>
  createStyles({
    button: {
      marginTop: "3%",
      width: "85%",
    },
  }),
);

interface State {
  email: string;
  password: string;
}


/**
 * Form with user email and password
 */
function LoginForm() {

  const [values, setValues] = React.useState<State>({
    email: "",
    password: "",
  });

  const handleChange = (prop: keyof State) => (event: React.ChangeEvent<HTMLInputElement>) => {
    setValues({ ...values, [prop]: event.target.value });
  };

  const classes = useStyles()

  return (
    <Fragment>
      <EmailField 
        handleChange={handleChange("email")}
        email={values.email}
      />
      <PasswordField
        handleChange={handleChange("password")}
        password={values.password}
      />
      <Button
        className={classes.button}
        variant="contained"
        color="primary"
      >
        Log in
      </Button>
    </Fragment>
  );
}

export default LoginForm
