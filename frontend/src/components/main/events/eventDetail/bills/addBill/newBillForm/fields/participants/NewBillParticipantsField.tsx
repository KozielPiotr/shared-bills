/**
 * Allows to choose participants for the new bill
 */

import React from "react";
import Typography from "@material-ui/core/Typography";

import useStyles from "../../styles";
import { ParticipantInterface } from "../../../../../../../../../interfaces/interfaces";
import SelectParticipants from "./NewBillSelectParticipants";

interface SelectParticipantsFieldProps {
  eventParticipants: ParticipantInterface[];
  handleSelectParticipants: (participant: ParticipantInterface) => void;
}

function SelectParticipantsField(props: SelectParticipantsFieldProps) {
  const classes = useStyles();

  return (
    <div className={classes.participantsChoice}>
      <Typography variant="h5" gutterBottom color="textSecondary">
        Choose participants
      </Typography>
      <hr />
      <SelectParticipants
        eventParticipants={props.eventParticipants}
        handleSelectParticipants={props.handleSelectParticipants}
      />
    </div>
  );
}

export default SelectParticipantsField;
