/**
 * Confirmation modal window. User can decide to abort adding new event or not
 */

import React from "react";

import Button from "@material-ui/core/Button";
import Modal from "@material-ui/core/Modal";
import Typography from "@material-ui/core/Typography";

import useStyles from "../styles";

interface AbortConfirmProps {
  handleCloseConfirmation: () => void;
  openConfirmation: boolean;
  handleConfirmAbort: () => void;
}

/**
 * Confirmation modal window
 */
function AbortConfirm(props: AbortConfirmProps) {
  const classes = useStyles();

  return (
    <Modal className={classes.modal} open={props.openConfirmation}>
      <div className={classes.paper}>
        <Typography
          className={classes.modalTitle}
          variant="h6"
          gutterBottom
          color="textSecondary"
        >
          Are you sure?
        </Typography>
        <Typography
          className={classes.modalTitle}
          variant="subtitle2"
          gutterBottom
          color="textSecondary"
        >
          The entered data will be lost
        </Typography>
        <hr />
        <div className={classes.modalButtons}>
          <Button
            onClick={props.handleConfirmAbort}
            variant="contained"
            color="primary"
          >
            Yes
          </Button>
          <Button
            onClick={props.handleCloseConfirmation}
            variant="contained"
            color="secondary"
          >
            No
          </Button>
        </div>
      </div>
    </Modal>
  );
}

export default AbortConfirm;
