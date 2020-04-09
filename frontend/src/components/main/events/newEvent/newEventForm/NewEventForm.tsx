/**
 * Form for new event with event name and paymaster name (will be also the first participant)
 */

import React from "react";

import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";

import useStyles from "../styles";
import NameField from "./NewEventFormName";
import OwnerField from "./NewEventFormOwner";
import eventService from "../../../../../services/events";

interface NewEventFormProps {
  handleOpenConfirmation: () => void;
  handleCloseAddEvent: () => void;
}

interface NewEventState {
  eventName: string;
  owner: string;
}

/**
 * Form for new event
 */
function NewEventForm(props: NewEventFormProps) {
  const classes = useStyles();

  const newEventInitialState = {
    eventName: "",
    owner: ""
  };

  const [newEventData, setNewEventData] = React.useState<NewEventState>(
    newEventInitialState
  );
  const [error, setError] = React.useState(false);

  const handleChange = (field: keyof NewEventState) => (
    event: React.ChangeEvent<HTMLInputElement>
  ) => {
    setNewEventData({ ...newEventData, [field]: event.target.value });
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    eventService.createEvent(newEventData).subscribe({
      error: error => {
        setError(error ? true : false);
      }
    });
    props.handleCloseAddEvent();
    eventService.fetchEvents();
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
            Event with this name already exists
          </Typography>
        </Grid>
      ) : null}

      <Grid container spacing={3}>
        <NameField
          error={!!error}
          eventName={newEventData.eventName}
          handleChange={handleChange("eventName")}
        />
        <OwnerField
          error={!!error}
          owner={newEventData.owner}
          handleChange={handleChange("owner")}
        />
        <Grid item xs={12}>
          <div className={classes.modalButtons}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              disabled={!newEventData.eventName || !newEventData.owner}
            >
              Confirm
            </Button>
            <Button
              onClick={props.handleOpenConfirmation}
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

export default NewEventForm;
