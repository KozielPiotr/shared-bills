import React from "react";

import { Button } from "@material-ui/core";

import useObservable from "../../../hooks/observable";
import eventService from "../../../services/events";

/**
 * List of events for main page
 */
function Events() {
  const events = useObservable(eventService.events());
  const handleClick = () => eventService.getEvents();

  console.log(events);
  return (
    <div>
      <h1>events placeholder</h1>
      <Button onClick={handleClick}>events</Button>
      {/* <p>{events}</p> */}
    </div>
  );
}

export default Events;
