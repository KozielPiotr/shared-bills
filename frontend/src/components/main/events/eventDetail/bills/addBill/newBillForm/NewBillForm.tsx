/**
 * Form for a new bill
 */

import React from "react";

import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";

import AmountField from "./fields/NewBillAmount";
import TitleField from "./fields/NewBillTitle";
import PaymasterField from "./fields/payer/NewBillPayer";
import SelectParticipantsField from "./fields/participants/NewBillParticipantsField";
import useStyles from "./styles";
import useObservable from "../../../../../../../hooks/observable";
import participantService from "../../../../../../../services/participants";
import selectParticipantsService from "../../../services";
import { ParticipantInterface } from "../../../../../../../interfaces/interfaces";
import billsService from "../../../../../../../services/bills";

interface NewBillFormProps {
  handleCloseAddBill: () => void;
  eventId: number;
  paymasterId: number;
  participantsUrl: string;
}

interface newBillState {
  title: string;
  amount: string;
  participants: number[];
  payer: number;
}

function NewBillForm(props: NewBillFormProps) {
  const classes = useStyles();

  const newBillInitialState = {
    participants: [],
    title: "",
    amount: "0",
    payer: props.paymasterId
  };

  const participants = useObservable(participantService.participants$);
  const included = useObservable(selectParticipantsService.included$);

  const [newBillData, setNewBillData] = React.useState<newBillState>(
    newBillInitialState
  );
  const [error, setError] = React.useState(false);

  /**
   * Checks if provided amount is correct. Decimals must be separated by a dot character.
   */
  const validateAmount = (amount: string) => {
    const re = /^[-+]?([0-9]*\.?[0-9]?[0-9])$/;
    re.test(String(amount)) ? setError(false) : setError(true);
  };

  const handleChange = (field: keyof newBillState) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    if (field === "amount") {
      validateAmount(event.target.value);
    }
    setNewBillData({
      ...newBillData,
      [field]: event.target.value
    });
  };

  const handleChangePayer = (payerId: number) => {
    setNewBillData({
      ...newBillData,
      payer: payerId
    });
  };

  /**
   * When user clicks a participant to include to the bill, the "included" observable is updated.
   * This observable is required to proper render of select list.
   * Also state of the new bill is updated. Selected participant's id is added or removed.
   *
   * @param {ParticipantInterface} participant - participant object selected from the list
   */
  const handleSelectParticipants = (participant: ParticipantInterface) => {
    if (included) {
      if (!included.includes(participant)) {
        selectParticipantsService.setIncluded([...included, participant]);
        setNewBillData({
          ...newBillData,
          participants: [...newBillData.participants, participant.id]
        });
      } else {
        let newIncluded: ParticipantInterface[] = [];
        for (let participantObject of included) {
          participantObject !== participant &&
            newIncluded.push(participantObject);
        }
        selectParticipantsService.setIncluded(newIncluded);

        let newStateIncluded = [];
        for (let participant of newIncluded) {
          newStateIncluded.push(participant.id);
        }
        setNewBillData({ ...newBillData, participants: newStateIncluded });
      }
    }
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    props.handleCloseAddBill();
    billsService.createBill(props.eventId, newBillData).subscribe();
  };

  React.useEffect(() => {
    participantService.fetchParticipants(props.participantsUrl);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return included !== undefined ? (
    <form onSubmit={handleSubmit}>
      <Grid container spacing={3}>
        <Grid className={classes.textGrid} item xs={4}>
          <TitleField handleChange={handleChange("title")} error={error} />
        </Grid>

        <Grid className={classes.textGrid} item xs={4}>
          <AmountField handleChange={handleChange("amount")} error={error} />
        </Grid>

        <Grid className={classes.textGrid} item xs={4}>
          <PaymasterField
            participants={participants}
            paymaster={newBillData.payer}
            handleChangePayer={handleChangePayer}
          />
        </Grid>

        <SelectParticipantsField
          eventParticipants={participants}
          handleSelectParticipants={handleSelectParticipants}
        />

        <Grid item xs={12}>
          <div className={classes.modalButtons}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              disabled={
                !newBillData.amount ||
                !newBillData.title ||
                !newBillData.participants
              }
            >
              Confirm
            </Button>
            <Button
              onClick={props.handleCloseAddBill}
              variant="contained"
              color="secondary"
            >
              Abort
            </Button>
          </div>
        </Grid>
      </Grid>
    </form>
  ) : null;
}

export default NewBillForm;
