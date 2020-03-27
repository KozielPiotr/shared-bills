/**
 * Events services
 */

import { BehaviorSubject } from "rxjs";
import { map } from "rxjs/operators";

import apiService from "./api";

class EventService {
  public events = new BehaviorSubject<any[]>([]);

  public fetchEvents = () => {
    apiService
      .get("/events/")
      .pipe(map(ajax => ajax.response))
      .subscribe(events => this.events.next(events));
  };
}

const eventService = new EventService();

export default eventService;
