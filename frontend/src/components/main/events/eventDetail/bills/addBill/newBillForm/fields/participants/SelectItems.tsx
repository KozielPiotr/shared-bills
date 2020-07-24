/**
 * ListItem with participant's name and checkbox to assign participant to the new bill or not
 */

import React, { Fragment } from "react";

import Divider from "@material-ui/core/Divider";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import Checkbox from "@material-ui/core/Checkbox";

import { ParticipantInterface } from "../../../../../../../../../interfaces/interfaces";
import selectParticipantsService from "../../../../../services";
import useObservable from "../../../../../../../../../hooks/observable";

interface ItemProps {
  participant: ParticipantInterface;
  key: number;
  includedParticipants: number[];
  handleSelectParticipants: (participant: ParticipantInterface) => void;
}

function Items(props: ItemProps) {
  const included = useObservable(selectParticipantsService.included$);

  return included ? (
    <Fragment>
      <ListItem
        button
        onClick={() => props.handleSelectParticipants(props.participant)}
      >
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
