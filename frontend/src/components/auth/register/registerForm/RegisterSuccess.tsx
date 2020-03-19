import React from "react";

import { makeStyles, Theme, createStyles } from "@material-ui/core/styles";
import { Button, Modal, Typography } from "@material-ui/core";

import authService, { AuthStage } from "../../../../services/auth";

interface SuccessProps {
  registeredUser: string;
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    modal: {
      display: "flex",
      alignItems: "center",
      justifyContent: "center"
    },
    paper: {
      position: "absolute",
      width: 400,
      backgroundColor: theme.palette.background.paper,
      border: "2px solid #000",
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
      textAlign: "center"
    }
  })
);

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
