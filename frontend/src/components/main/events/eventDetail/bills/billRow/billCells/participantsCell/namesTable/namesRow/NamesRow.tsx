/**
 * Table row with participant's name and his or her share of the bill
 */

import React from "react";

import { BehaviorSubject } from "rxjs";
import { map } from "rxjs/operators";

import TableRow from "@material-ui/core/TableRow";

import useObservable from "../../../../../../../../../../hooks/observable";
import apiService from "../../../../../../../../../../services/api";
import NameCell from "./namesTableCells/NameCell";
import AmountCell from "./namesTableCells/AmountCell";

interface NameRowProps {
  participantId: number;
  eventId: number;
  amount: number;
  currency: string;
  billUrl: string;
  key: number;
}

function NameRow(props: NameRowProps) {
  const participant$ = new BehaviorSubject<any[]>([]);
  const participant = useObservable(participant$);

  const fetchParticipantById = () => {
    apiService
      .get(`/events/${props.eventId}/participants/${props.participantId}/`)
      .pipe(map(ajax => ajax.response))
      .subscribe(participant => {
        participant$.next(participant);
      });
  };

  React.useEffect(() => {
    fetchParticipantById();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);
  return participant && participant.username ? (
    <TableRow>
      <NameCell participant={participant.username} />
      <AmountCell amount={props.amount} currency={props.currency} />
    </TableRow>
  ) : null;
}

export default NameRow;
