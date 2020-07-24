/**
 * Styles for EventDetail component
 */

import {
  withStyles,
  Theme,
  createStyles,
  makeStyles
} from "@material-ui/core/styles";
import TableCell from "@material-ui/core/TableCell";

const useStyles = makeStyles(() => ({
  root: {
    width: "100%",
    marginTop: "3%"
  },
  title: {
    paddingTop: "1%",
    paddingBottom: "1%"
  },
  tabPanel: {
    backgroundColor: "#f5f5f5"
  },
  tableContainer: {
    marginTop: "3%"
  },
  table: {
    width: "100%"
  }
}));

export const HeaderTableCell = withStyles((theme: Theme) =>
  createStyles({
    head: {
      backgroundColor: theme.palette.info.main,
      color: theme.palette.common.white
    },
    body: {
      fontSize: 14
    }
  })
)(TableCell);

export default useStyles;
