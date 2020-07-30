/**
 * Modal window with a form to create event's new bill
 */

import React from "react";

import Modal from "@material-ui/core/Modal";
import Typography from "@material-ui/core/Typography";

import NewBillForm from "./newBillForm/NewBillForm";

import useStyles from "../styles";

interface AddBillProps {
  open: boolean;
  handleCloseAddBill: () => void;
  eventId: number;
  paymasterId: number;
  participantsUrl: string;
}

/**
 * Modal window for new participant form
 */
function AddBill(props: AddBillProps) {
  const classes = useStyles();

  return (
    <div style={{alignContent: "center"}}>
      <Modal className={classes.modal} open={props.open}>
        <div className={classes.paper}>
          <Typography
            className={classes.modalTitle}
            variant="h4"
            gutterBottom
            color="textSecondary"
          >
            New bill
          </Typography>
          <hr />
          <NewBillForm
            handleCloseAddBill={props.handleCloseAddBill}
            eventId={props.eventId}
            paymasterId={props.paymasterId}
            participantsUrl={props.participantsUrl}
          />
        </div>
      </Modal>
    </div>
  );
}

export default AddBill;
