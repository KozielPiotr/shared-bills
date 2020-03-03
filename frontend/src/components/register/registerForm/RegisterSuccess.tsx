import React from "react";
import { Link } from "react-router-dom";

import { Typography } from "@material-ui/core";

import { SuccessProps } from "./utils/interfaces";

/**
 * Success message if register was correct
 */
export default function RegisterSuccess(props: SuccessProps) {
  return (
    <Typography variant="h5" gutterBottom color="textSecondary">
      {props.registeredUser} registered.
      <Link to="/">Login</Link>
    </Typography>
  );
}
