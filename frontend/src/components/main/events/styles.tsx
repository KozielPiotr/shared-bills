/**
 * Styles for Event component
 */

import { createStyles, makeStyles, Theme } from "@material-ui/core/styles";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    title: {
      textAlign: "left",
      marginTop: "2%",
      marginBottom: "1%"
    },
    button: {
      margin: theme.spacing(1)
    },
    progress: {
      width: "100%",
      "& > * + *": {
        marginTop: theme.spacing(2)
      }
    }
  })
);

export default useStyles;
