/**Detail view of chosen event */

import React from "react";
import { useParams } from "react-router-dom";

import SwipeableViews from "react-swipeable-views";
import { useTheme } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Paper from "@material-ui/core/Paper";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";

import useObservable from "../../../../hooks/observable";
import eventService from "../../../../services/events";
import { localStorageService } from "../../../../services/storage";
import useStyles from "./styles";
import TabPanel from "./tabPanel/TabPanel";
import Participants from "./participants/Participants";
import Bills from "./bills/Bills";

function a11yProps(index: any) {
  return {
    key: `full-width-tab-${index}`,
    "aria-controls": `full-width-tabpanel-${index}`
  };
}

/**
 * Component with a detail view of the event
 */
function EventDetail() {
  const classes = useStyles();
  const theme = useTheme();
  const event = useObservable(eventService.event$);
  const { id } = useParams();
  const [value, setValue] = React.useState(0);
  const tabs = ["Participants", "Bills", "Payments", "Summary"];

  const handleChange = (event: React.ChangeEvent<{}>, newValue: number) => {
    setValue(newValue);
  };

  const handleChangeIndex = (index: number) => {
    setValue(index);
  };

  event === null && eventService.fetchEventById(id);

  React.useEffect(() => {
    eventService.fetchEvent(localStorageService.getEventUrl());
  }, []);

  return event != null ? (
    <div>
      <Typography className={classes.title} variant="h4">
        {event.name}
      </Typography>
      <Paper className={classes.root} elevation={3}>
        <AppBar position="static" color="default">
          <Tabs
            value={value}
            onChange={handleChange}
            indicatorColor="primary"
            textColor="primary"
            variant="fullWidth"
          >
            {tabs.map((tab, index) => (
              <Tab label={tab} {...a11yProps(index)}></Tab>
            ))}
          </Tabs>
        </AppBar>
        <SwipeableViews
          axis={theme.direction === "rtl" ? "x-reverse" : "x"}
          index={value}
          onChangeIndex={handleChangeIndex}
        >
          <TabPanel value={value} index={0} dir={theme.direction}>
            <Participants
              participantsUrl={event.participants_url}
              billsUrl={event.bills_url}
              paymasterId={event.paymaster.id}
              paymentsUrl={event.payments_url}
              eventId={event.id}
            />
          </TabPanel>
          <TabPanel value={value} index={1} dir={theme.direction}>
            <Bills
              billsUrl={event.bills_url}
              eventId={event.id}
              participantsUrl={event.participants_url}
              paymasterId={event.paymaster.id}
            />
          </TabPanel>
          <TabPanel value={value} index={2} dir={theme.direction}>
            List of payments
          </TabPanel>
          <TabPanel value={value} index={3} dir={theme.direction}>
            Summary with info who owns whom, how much and for what
          </TabPanel>
        </SwipeableViews>
      </Paper>
    </div>
  ) : null;
}

export default EventDetail;
