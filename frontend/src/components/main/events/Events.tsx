/**
 * Component with all current user's events
 */

import React from "react";

import { makeStyles, createStyles, Theme } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import GridList from "@material-ui/core/GridList";
import AddCircleIcon from "@material-ui/icons/AddCircle";

import useObservable from "../../../hooks/observable";
import eventService from "../../../services/events";
import EventCard from "./eventCard/EventCard";

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    title: {
      textAlign: "left",
      marginTop: "2%",
      marginBottom: "1%"
    },
    button: {
      margin: theme.spacing(1)
    }
  })
);

/**
 * List of events for main page
 */
function Events() {
  React.useEffect(eventService.fetchEvents, []);
  const classes = useStyles();
  const events = useObservable(eventService.events);

  return (
    <div>
      <div className={classes.title}>
        Events
        <Button
          variant="outlined"
          color="primary"
          className={classes.button}
          endIcon={<AddCircleIcon />}
        >
          add
        </Button>
      </div>
      <hr />
      <GridList cellHeight={180}>
        {events && events.length > 0 ? (
          events.map((event: any) => <EventCard key={event.id} event={event} />)
        ) : (
          <p>no events</p>
        )}
      </GridList>
    </div>
  );
}

export default Events;
