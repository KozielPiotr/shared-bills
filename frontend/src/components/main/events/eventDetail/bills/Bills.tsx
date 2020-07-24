/**
 * Tab with list of event's bills
 */

import React from "react";

import Button from "@material-ui/core/Button";
import AddCircleOutlineIcon from "@material-ui/icons/AddCircleOutline";
import Table from "@material-ui/core/Table";
import TableCell from "@material-ui/core/TableCell";
import TableBody from "@material-ui/core/TableBody";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import Paper from "@material-ui/core/Paper";

import useStyles, { HeaderTableCell } from "../styles";
import BillRow from "./billRow/BillRow";
import AddBill from "./addBill/AddBill";

import billsService from "../../../../../services/bills";
import useObservable from "../../../../../hooks/observable";
import { BillInterface } from "../../../../../interfaces/interfaces";

interface BillsProps {
  billsUrl: string;
  eventId: number;
  participantsUrl: string;
  paymasterId: number;
}

/**
 * Component with list of event's bills
 */
function Bills(props: BillsProps) {
  const classes = useStyles();

  const bills = useObservable(billsService.bills$);
  const [openAddBill, setOpenAddBill] = React.useState(false);

  const handleOpenAddBill = () => {
    setOpenAddBill(true);
  };

  const handleCloseAddBill = () => {
    setOpenAddBill(false);
  };

  const headerCells = ["Amount", "Participants", "Payer"];

  React.useEffect(() => {
    billsService.fetchBills(props.billsUrl);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return bills != null ? (
    <TableContainer className={classes.tableContainer} component={Paper}>
      <Table className={classes.table}>
        <TableHead>
          <TableRow>
            <HeaderTableCell>Bill</HeaderTableCell>
            {headerCells.map(cell => (
              <HeaderTableCell key={cell} align="right">
                {cell}
              </HeaderTableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {bills.map((bill: BillInterface) => (
            <BillRow
              billTitle={bill.title}
              amount={bill.amount}
              currency={bill.amount_currency}
              eventId={props.eventId}
              payerId={bill.payer}
              billUrl={bill.url}
              participantsUrl={props.participantsUrl}
              key={bill.id}
            />
          ))}
          <TableRow>
            <TableCell colSpan={headerCells.length + 1} align="center">
              <Button
                variant="contained"
                color="primary"
                startIcon={<AddCircleOutlineIcon />}
                onClick={handleOpenAddBill}
              >
                Add Bill
              </Button>
              <AddBill
                open={openAddBill}
                handleCloseAddBill={handleCloseAddBill}
                eventId={props.eventId}
                paymasterId={props.paymasterId}
                participantsUrl={props.participantsUrl}
              />
            </TableCell>
          </TableRow>
        </TableBody>
      </Table>
    </TableContainer>
  ) : null;
}

export default Bills;
