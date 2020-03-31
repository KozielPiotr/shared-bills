/**
 * Styles for Main component
 */

import { createStyles, makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(() =>
  createStyles({
    root: {
      flexGrow: 1,
      textAlign: "center",
      backgroundColor: "#f5f5f5"
    },
    title: {
      flexGrow: 1,
      textAlign: "center"
    },
    content: {
      marginLeft: "5%",
      marginRight: "5%"
    }
  })
);

export default useStyles;
