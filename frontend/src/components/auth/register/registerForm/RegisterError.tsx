import React from "react";

import { AjaxError } from "rxjs/ajax";

import { Typography } from "@material-ui/core";

/**
 * Error message if register form is filled incorrectly or api returned error
 */

interface ErrorFieldProps {
  error: AjaxError;
}

/**
 * Renders Ajax response errors
 */
export default function RegisterError(props: ErrorFieldProps) {
  return (
    <Typography variant="subtitle2" color="error" gutterBottom>
      {props.error.response.email && "email already registered"}
    </Typography>
  );
}
