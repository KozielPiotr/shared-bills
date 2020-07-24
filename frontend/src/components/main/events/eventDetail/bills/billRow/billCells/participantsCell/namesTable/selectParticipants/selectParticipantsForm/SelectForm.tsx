/**
 * Form for bill's participant choice
 */

import React from "react";

import List from "@material-ui/core/List";
import Button from "@material-ui/core/Button";

import Items from "./SelectFormItems";

import {
  ParticipantInterface,
  BillInterface
} from "../../../../../../../../../../../interfaces/interfaces";
import BillsService from "../../../../../../../../../../../services/bills";
import selectParticipantsService from "../../../../../../../services";
import useStyles from "../styles";

interface SelectFormProps {
  eventParticipants: ParticipantInterface[];
  includedParticipants: ParticipantInterface[];
  handleOpen: () => void;
  bill: BillInterface;
}

function SelectForm(props: SelectFormProps) {
  const classes = useStyles();

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    let newBill = props.bill;
    const participantList = [
      ...selectParticipantsService.included$
        .getValue()
        .map(participant => participant.id)
    ];
    newBill.participants = participantList;
    BillsService.updateBill(props.bill.url, newBill).subscribe(() =>
      props.handleOpen()
    );
  };

  React.useEffect(() => {
    selectParticipantsService.included$.next(props.includedParticipants);
  });

  return (
    <form onSubmit={handleSubmit}>
      <div className={classes.listRoot}>
        <List className={classes.includedList}>
          {props.eventParticipants.map(participant => (
            <Items participant={participant} key={participant.id} />
          ))}
        </List>
        <div className={classes.modalButtons}>
          <Button type="submit" variant="contained" color="primary">
            Confirm
          </Button>
          <Button
            onClick={props.handleOpen}
            variant="contained"
            color="secondary"
          >
            Abort
          </Button>
        </div>
      </div>
    </form>
  );
}

export default SelectForm;
