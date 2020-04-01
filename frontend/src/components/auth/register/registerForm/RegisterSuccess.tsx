import React from "react";

import { Button, Modal, Typography } from "@material-ui/core";

import authService, { AuthStage } from "../../../../services/auth";
import useStyles from "./styles";

interface SuccessProps {
  registeredUser: string;
}

/**
 * Modal with success message and button to login page if registration was correct
 */
export default function RegisterSuccess(props: SuccessProps) {
  const classes = useStyles();

  return (
    <Modal
      className={classes.modal}
      aria-labelledby="simple-modal-title"
      aria-describedby="simple-modal-description"
      open={true}
    >
      <div className={classes.paper}>
        <Typography variant="h5" gutterBottom color="textSecondary">
          {props.registeredUser} registered.{" "}
          <Button
            onClick={() => authService.setAuthAction(AuthStage.Login)}
            color="primary"
            variant="contained"
          >
            Login
          </Button>
        </Typography>
      </div>
    </Modal>
  );
}
