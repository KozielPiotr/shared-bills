/**
 * Styles for Register component
 */

import { createStyles, makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles(() =>
  createStyles({
    grid: {
      textAlign: "center",
      justifyContent: "center",
      alignContent: "center",
      backgroundColor: "#f5f5f5",
      flexWrap: "nowrap",
      paddingLeft: "15%",
      paddingRight: "15%"
    },
    paper: {
      margin: 0,
      paddingTop: "3%",
      paddingBottom: "3%",
      marginLeft: "25%",
      marginRight: "25%"
    },
    typography: {
      padding: "1%",
      textAlign: "center"
    }
  })
);

export default useStyles;
