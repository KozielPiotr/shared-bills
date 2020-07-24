/**
 * Modal window with a form to create event's new participant
 */

import React from "react";

import Modal from "@material-ui/core/Modal";
import Typography from "@material-ui/core/Typography";

import useStyles from "../styles";
import NewParticipantForm from "./newParticipantForm/NewParticipantForm";

interface AddParticipantProps {
  open: boolean;
  handleCloseAddParticipant: () => void;
  eventId: number;
}

/**
 * Modal window for new participant form
 */
function AddParticipant(props: AddParticipantProps) {
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
            New participant
          </Typography>
          <hr />
          <NewParticipantForm
            handleCloseAddParticipant={props.handleCloseAddParticipant}
            eventId={props.eventId}
          />
        </div>
      </Modal>
    </div>
  );
}

export default AddParticipant;
