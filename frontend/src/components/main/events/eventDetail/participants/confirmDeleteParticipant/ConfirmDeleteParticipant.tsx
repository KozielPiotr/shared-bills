/**
 * Modal with the participant deletion confirmation
 */

import React from "react";

import Modal from "@material-ui/core/Modal";
import Typography from "@material-ui/core/Typography";

import useStyles from "../styles";
import Grid from "@material-ui/core/Grid";
import Button from "@material-ui/core/Button";

import participantService from "../../../../../../services/participants";

interface ConfirmDeleteProps {
  participantUrl: string;
  open: boolean;
  handleCloseDelete: () => void;
}

function ConfirmDelete(props: ConfirmDeleteProps) {
  const classes = useStyles();
  const [error, setError] = React.useState(false);

  const handleConfirm = () => {
    participantService.deleteParticipant(props.participantUrl).subscribe(
      () => props.handleCloseDelete(),
      error => setError(true)
    );
  };

  return (
    <Modal className={classes.modal} open={props.open}>
      <div className={classes.paper}>
        {!error ? (
          <Typography
            className={classes.modalTitle}
            variant="h4"
            gutterBottom
            color="textSecondary"
          >
            Are you sure you want to delete this participant?
          </Typography>
        ) : (
          <Typography
            className={classes.errorMsg}
            variant="h6"
            gutterBottom
            color="error"
          >
            Could not delete this participant.
            <br />
            Remove this participant from it's bills and payments first.
          </Typography>
        )}
        <hr />
        <Grid item xs={12}>
          <div className={classes.modalButtons}>
            {!error && (
              <Button
                onClick={handleConfirm}
                type="submit"
                variant="contained"
                color="primary"
              >
                Yes
              </Button>
            )}
            <Button
              onClick={() => {
                props.handleCloseDelete();
                setError(false);
              }}
              variant="contained"
              color="secondary"
            >
              Abort
            </Button>
          </div>
        </Grid>
      </div>
    </Modal>
  );
}

export default ConfirmDelete;
