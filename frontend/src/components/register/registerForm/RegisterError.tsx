import React from "react";

import { Typography } from "@material-ui/core";

/**
 * Error message if register form is filled incorrectly or api returned error
 */
export default function RegisterError() {
  return (
    <Typography variant="subtitle2" color="error" gutterBottom>
      Wrong email or password.
      <br />
      Email has to be in right email format.
      <br />
      Password must be at least 8 characters long.
      <br />
    </Typography>
  );
}
