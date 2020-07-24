/**
 * Allows user to choose bill's participants
 */

import React from "react";
import Modal from "@material-ui/core/Modal";
import Typography from "@material-ui/core/Typography";

import useStyles from "./styles";
import {
  ParticipantInterface,
  BillInterface
} from "../../../../../../../../../../interfaces/interfaces";
import SelectForm from "./selectParticipantsForm/SelectForm";

interface SelectParticipantsProps {
  open: boolean;
  bill: BillInterface;
  handleOpen: () => void;
  eventParticipants: ParticipantInterface[];
  includedParticipants: number[];
}

function SelectParticipants(props: SelectParticipantsProps) {
  const classes = useStyles();

  const searchIncluded = () => {
    let includedParticipants: ParticipantInterface[] = [];
    props.eventParticipants.map(
      participant =>
        props.includedParticipants.includes(participant.id) &&
        includedParticipants.push(participant)
    );
    return includedParticipants;
  };
  const included = searchIncluded();

  return (
    <div>
      <Modal className={classes.modal} open={props.open}>
        <div className={classes.paper}>
          <Typography
            className={classes.modalTitle}
            variant="h5"
            gutterBottom
            color="textSecondary"
          >
            Choose participants
          </Typography>
          <hr />
          <SelectForm
            bill={props.bill}
            eventParticipants={props.eventParticipants}
            includedParticipants={included}
            handleOpen={props.handleOpen}
          />
        </div>
      </Modal>
    </div>
  );
}

export default SelectParticipants;
