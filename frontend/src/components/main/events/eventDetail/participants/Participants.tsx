/**
 * Tab with list of event's participants
 */

import React from "react";

import Button from "@material-ui/core/Button";
import AddCircleOutlineIcon from "@material-ui/icons/AddCircleOutline";
import Table from "@material-ui/core/Table";
import TableCell from "@material-ui/core/TableCell";
import TableBody from "@material-ui/core/TableBody";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

import participantService from "../../../../../services/participants";
import billsService from "../../../../../services/bills";
import paymentsService from "../../../../../services/payments";
import useObservable from "../../../../../hooks/observable";
import { ParticipantInterface } from "../../../../../interfaces/interfaces";
import useStyles, { HeaderTableCell } from "../styles";
import ParticipantRow from "./participantRow/ParticipantRow";
import AddParticipant from "./addParticipant/AddParticipant";
import ConfirmDelete from "./confirmDeleteParticipant/ConfirmDeleteParticipant";

interface ParticipantsProps {
  participantsUrl: string;
  billsUrl: string;
  paymentsUrl: string;
  paymasterId: number;
  eventId: number;
}

/**
 * Component with list of event's participants
 */
function Participants(props: ParticipantsProps) {
  const classes = useStyles();

  const participants = useObservable(participantService.participants$);
  const bills = useObservable(billsService.bills$);
  const payments = useObservable(paymentsService.payments$);

  const [openAddParticipant, setOpenAddParticipant] = React.useState(false);
  const [openDelete, setOpenDelete] = React.useState(false);
  const [participantToDeleteUrl, setParticipantToDeleteUrl] = React.useState(
    ""
  );

  const handleOpenAddParticipant = () => {
    setOpenAddParticipant(true);
  };
  const handleCloseAddParticipant = () => {
    setOpenAddParticipant(false);
  };

  const handleOpenDelete = (participantUrl: string) => {
    setOpenDelete(true);
    setParticipantToDeleteUrl(participantUrl);
  };

  const handleCloseDelete = () => {
    setOpenDelete(false);
  };

  const headerCells = [
    "Number of bills",
    "Number of payments as acquirer",
    "Number of payments as issuer"
  ];

  React.useEffect(() => {
    billsService.fetchBills(props.billsUrl);
    paymentsService.fetchPayments(props.paymentsUrl);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  React.useEffect(() => {
    participantService.fetchParticipants(props.participantsUrl);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [openDelete === false]);

  return participants != null && bills != null && payments != null ? (
    <TableContainer className={classes.tableContainer} component={Paper}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <HeaderTableCell>Participant</HeaderTableCell>
            {headerCells.map(cell => (
              <HeaderTableCell key={cell} align="right">
                {cell}
              </HeaderTableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {participants.map((participant: ParticipantInterface) => (
            <ParticipantRow
              participant={participant}
              paymasterId={props.paymasterId}
              bills={bills}
              payments={payments}
              handleOpenDelete={handleOpenDelete}
              key={participant.id}
            />
          ))}
          <ConfirmDelete
            open={openDelete}
            participantUrl={participantToDeleteUrl}
            handleCloseDelete={handleCloseDelete}
          />
          <TableRow>
            <TableCell colSpan={headerCells.length + 1} align="center">
              <Button
                variant="contained"
                color="primary"
                startIcon={<AddCircleOutlineIcon />}
                onClick={handleOpenAddParticipant}
              >
                Add participant
              </Button>
              <AddParticipant
                open={openAddParticipant}
                handleCloseAddParticipant={handleCloseAddParticipant}
                eventId={props.eventId}
              />
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
  ) : null;
}

export default Participants;
