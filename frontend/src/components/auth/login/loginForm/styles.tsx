/**
 * Styles for Login form
 */

import { createStyles, makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(() =>
  createStyles({
    textFieldGrid: {
      paddingTop: "3%"
    },
    textField: {
      width: "85%"
    },
    button: {
      marginTop: "3%",
      width: "85%"
    }
  })
);

export default useStyles;
