/**
 * Styles for Register component
 */

import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    button: {
      marginTop: "3%",
      width: "85%"
    },
    textFieldGrid: {
      paddingTop: "3%"
    },
    textField: {
      width: "85%"
    },
    modal: {
      display: "flex",
      alignItems: "center",
      justifyContent: "center"
    },
    paper: {
      position: "absolute",
      width: 400,
      backgroundColor: theme.palette.background.paper,
      border: "2px solid #000",
      boxShadow: theme.shadows[5],
      padding: theme.spacing(2, 4, 3),
      textAlign: "center"
    }
  })
);

export default useStyles;
