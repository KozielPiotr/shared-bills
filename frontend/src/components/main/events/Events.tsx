import React from "react";

import { Button } from "@material-ui/core";

import useObservable from "../../../hooks/observable";
import eventService from "../../../services/events";

/**
 * List of events for main page
 */
function Events() {
  React.useEffect(eventService.fetchEvents, []);
  const events = useObservable(eventService.events);

  console.log(events);
  return (
    <div>
      <h1>events placeholder</h1>
      <Button onClick={eventService.fetchEvents}>events</Button>
      {events && events.length > 0 ? events.map((event: { id: React.ReactNode; }) => <p>{event.id}</p>) : <p>no events</p>}
    </div>
  );
}

export default Events;
