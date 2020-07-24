/**
 * Styles for new bill form components
 */

import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";
const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    textField: {
      width: "85%"
    },
    textGrid: {
      marginTop: "3%"
    },
    participantsChoice: {
      backgroundColor: theme.palette.background.paper,
      padding: theme.spacing(2, 4, 3),
      textAlign: "center"
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
