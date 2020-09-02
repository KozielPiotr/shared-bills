/**
 * Form for bill's participant choice
 */

import React from "react";

import List from "@material-ui/core/List";

import Items from "./SelectItems";

import { ParticipantInterface } from "../../../../../../../../../interfaces/interfaces";
import selectParticipantsService from "../../../../../services";
import useStyles from "../../styles";
import useObservable from "../../../../../../../../../hooks/observable";

interface SelectParticipantsProps {
  eventParticipants: ParticipantInterface[];
  handleSelectParticipants: (participant: ParticipantInterface) => void;
}

function SelectParticipants(props: SelectParticipantsProps) {
  const classes = useStyles();

  const includedParticipants = useObservable(
    selectParticipantsService.included$
  );

  return props.eventParticipants ? (
    <div className={classes.listRoot}>
      <List className={classes.includedList}>
        {props.eventParticipants.map(participant => (
          <Items
            participant={participant}
            key={participant.id}
            includedParticipants={includedParticipants}
            handleSelectParticipants={props.handleSelectParticipants}
          />
        ))}
      </List>
    </div>
  ) : null;
}

export default SelectParticipants;
