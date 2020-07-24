/**
 * Form for a new participant with participant name
 */

import React from "react";

import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";

import useStyles from "../../styles";
import NameField from "./NewEventParticipantName";
import participantsService from "../../../../../../../services/participants";

interface NewParticipantFormProps {
  handleCloseAddParticipant: () => void;
  eventId: number;
}

interface NewParticipantState {
  participantName: string;
}

/**
 * Form for new participant
 */
function NewParticipantForm(props: NewParticipantFormProps) {
  const classes = useStyles();

  const newParticipantInitialState = {
    participantName: ""
  };

  const [newParticipantData, setNewParticipantData] = React.useState<
    NewParticipantState
  >(newParticipantInitialState);
  const [error, setError] = React.useState(false);

  const handleChange = (field: keyof NewParticipantState) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setNewParticipantData({
      ...newParticipantData,
      [field]: event.target.value
    });
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    participantsService
      .createParticipant(newParticipantData, props.eventId)
      .subscribe(
        () => props.handleCloseAddParticipant(),
        error => setError(true)
      );
  };

  return (
    <form onSubmit={handleSubmit}>
      {error ? (
        <Grid container spacing={3}>
          <Typography
            className={classes.errorMsg}
            variant="h6"
            gutterBottom
            color="error"
          >
            Participant with this name already exists
          </Typography>
        </Grid>
      ) : null}

      <Grid container spacing={3}>
        <NameField
          error={!!error}
          eventName={newParticipantData.participantName}
          handleChange={handleChange("participantName")}
        />
        <Grid item xs={12}>
          <div className={classes.modalButtons}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              disabled={!newParticipantData.participantName}
            >
              Confirm
            </Button>
            <Button
              onClick={props.handleCloseAddParticipant}
              variant="contained"
              color="secondary"
            >
              Abort
            </Button>
          </div>
        </Grid>
      </Grid>
    </form>
  );
}

export default NewParticipantForm;
