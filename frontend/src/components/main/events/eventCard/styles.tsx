/**
 * Styles for Event card
 */

import { makeStyles, createStyles } from "@material-ui/core/styles";
import { indigo } from "@material-ui/core/colors";

const useStyles = makeStyles(() =>
  createStyles({
    root: {
      width: "15%",
      margin: "2%"
    },
    media: {
      height: 0,
      paddingTop: "56.25%"
    },
    avatar: {
      backgroundColor: indigo[500]
    }
  })
);

export default useStyles;
