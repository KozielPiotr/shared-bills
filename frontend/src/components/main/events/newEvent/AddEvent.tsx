/**
 * With this component user can add a new event
 */

import React from "react";

import Modal from "@material-ui/core/Modal";
import Typography from "@material-ui/core/Typography";

import useStyles from "./styles";
import NewEventForm from "./newEventForm/NewEventForm";
import AbortConfirm from "./abortConfirm/AbortConfirm";

interface AddEventProps {
  open: boolean;
  handleCloseAddEvent: () => void;
  handleOpenConfirmation: () => void;
  handleCloseConfirmation: () => void;
  handleConfirmAbort: () => void;
  openConfirmation: boolean;
}

/**
 * Modal window for new event form
 */
function AddEvent(props: AddEventProps) {
  const classes = useStyles();

  return (
    <div>
      <Modal className={classes.modal} open={props.open}>
        <div className={classes.paper}>
          <Typography
            className={classes.modalTitle}
            variant="h4"
            gutterBottom
            color="textSecondary"
          >
            New event
          </Typography>
          <hr />
          <NewEventForm
            handleOpenConfirmation={props.handleOpenConfirmation}
            handleCloseAddEvent={props.handleCloseAddEvent}
          />
        </div>
      </Modal>
      <AbortConfirm
        openConfirmation={props.openConfirmation}
        handleCloseConfirmation={props.handleCloseConfirmation}
        handleConfirmAbort={props.handleConfirmAbort}
      />
    </div>
  );
}

export default AddEvent;
