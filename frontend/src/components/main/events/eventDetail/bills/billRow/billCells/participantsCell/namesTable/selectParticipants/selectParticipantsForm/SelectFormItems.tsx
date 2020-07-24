/**
 * ListItem with participant's name and checkbox to assign participant to bill or not
 */

import React, { Fragment } from "react";

import Divider from "@material-ui/core/Divider";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import Checkbox from "@material-ui/core/Checkbox";

import { ParticipantInterface } from "../../../../../../../../../../../interfaces/interfaces";
import selectParticipantsService from "../../../../../../../services";
import useObservable from "../../../../../../../../../../../hooks/observable";

interface ItemProps {
  participant: ParticipantInterface;
  key: number;
}

function Items(props: ItemProps) {
  const included = useObservable(selectParticipantsService.included$);

  const handleClick = () => {
    if (!included.includes(props.participant)) {
      selectParticipantsService.setIncluded([...included, props.participant]);
    } else {
      let newIncluded: ParticipantInterface[] = [];
      for (let participantObject of included) {
        participantObject !== props.participant &&
          newIncluded.push(participantObject);
      }
      selectParticipantsService.setIncluded(newIncluded);
    }
  };
  return included ? (
    <Fragment>
      <ListItem button onClick={() => handleClick()}>
        <ListItemIcon>
          <Checkbox checked={included.includes(props.participant)} />
        </ListItemIcon>
        <ListItemText primary={props.participant.username} />
      </ListItem>
      <Divider />
    </Fragment>
  ) : null;
}

export default Items;
