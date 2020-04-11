/**
 * With this component user can add a new event
 */

import React from "react";

import Modal from "@material-ui/core/Modal";
import Typography from "@material-ui/core/Typography";

import useStyles from "./styles";
import NewEventForm from "./newEventForm/NewEventForm";

interface AddEventProps {
  open: boolean;
  handleCloseAddEvent: () => void;
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
          <NewEventForm handleCloseAddEvent={props.handleCloseAddEvent} />
        </div>
      </Modal>
    </div>
  );
}

export default AddEvent;
