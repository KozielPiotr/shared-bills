/**
 * Events services
 */

import { BehaviorSubject, Observable } from "rxjs";
import { map } from "rxjs/operators";

import apiService from "./api";

class EventService {
  public events$ = new BehaviorSubject<any[]>([]);

  public fetchEvents = () => {
    apiService
      .get("/events/")
      .pipe(map(ajax => ajax.response))
      .subscribe(events => this.events$.next(events));
  };

  public createEvent = (eventData: {
    eventName: string;
    owner: string;
  }): Observable<any> => {
    const body = {
      paymaster: {
        username: eventData.owner
      },
      name: eventData.eventName
    };
    return apiService.post("/events/", body).pipe(map(ajax => ajax.response));
  };
}

const eventService = new EventService();

export default eventService;
