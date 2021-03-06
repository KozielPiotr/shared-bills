/**
 * Component with all current user's events
 */

import React from "react";

import Button from "@material-ui/core/Button";
import GridList from "@material-ui/core/GridList";
import AddCircleIcon from "@material-ui/icons/AddCircle";
import LinearProgress from "@material-ui/core/LinearProgress";

import useStyles from "./styles";
import useObservable from "../../../hooks/observable";
import eventService from "../../../services/events";
import EventCard from "./eventCard/EventCard";
import AddEvent from "./newEvent/AddEvent";

/**
 * List of events for main page
 */
function Events() {
  React.useEffect(eventService.fetchEvents, []);

  const classes = useStyles();
  const events = useObservable(eventService.events$);
  const loading = useObservable(eventService.eventsLoading$);

  const [openAddEvent, setOpenAddEvent] = React.useState(false);

  const handleOpenAddEvent = () => {
    setOpenAddEvent(true);
  };
  const handleCloseAddEvent = () => {
    setOpenAddEvent(false);
  };

  return (
    <div>
      <div className={classes.title}>
        Events
        <Button
          onClick={handleOpenAddEvent}
          variant="outlined"
          color="primary"
          className={classes.button}
          endIcon={<AddCircleIcon />}
        >
          add
        </Button>
      </div>
      <hr />
      {loading ? <LinearProgress /> : null}
      <GridList cellHeight={180}>
        {events && events.length > 0 ? (
          events.map((event: any) => <EventCard key={event.id} event={event} />)
        ) : (
          <p>no events</p>
        )}
      </GridList>
      <AddEvent open={openAddEvent} handleCloseAddEvent={handleCloseAddEvent} />
    </div>
  );
}

export default Events;
