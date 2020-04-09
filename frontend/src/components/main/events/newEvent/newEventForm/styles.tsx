/**
 * Styles for NewEventForm components
 */

import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    textField: {
      width: "85%"
    },
    textGrid: {
      marginTop: "3%"
    }
  })
);

export default useStyles;
