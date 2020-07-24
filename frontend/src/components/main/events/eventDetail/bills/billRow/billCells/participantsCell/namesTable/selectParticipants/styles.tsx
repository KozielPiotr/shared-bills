/**
 * Styles for SelectParticipant component
 */

import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    modal: {
      display: "flex",
      alignItems: "center",
      justifyContent: "center"
    },
    paper: {
      position: "absolute",
      maxWidth: "40%",
      backgroundColor: theme.palette.background.paper,
      border: "2px solid #000",
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
      textAlign: "center"
    },
    modalTitle: {
      textAlign: "left"
    },
    modalButtons: {
      display: "flex",
      justifyContent: "space-around"
    },
    errorMsg: {
      textAlign: "center",
      marginTop: "3%"
    },
    listRoot: {
      textAlign: "left",
      adding: "4%"
    },
    includedList: {
      width: "90%"
    }
  })
);

export default useStyles;
