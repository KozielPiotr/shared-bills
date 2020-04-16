/**
 * Events services
 */

import { BehaviorSubject, Observable } from "rxjs";
import { map, tap } from "rxjs/operators";

import apiService from "./api";

/**
 * Manages events
 */
class EventService {
  public events$ = new BehaviorSubject<any[]>([]);
  public eventsLoading$ = new BehaviorSubject<boolean>(false);

  public fetchEvents = () => {
    this.eventsLoading$.next(true);
    apiService
      .get("/events/")
      .pipe(map(ajax => ajax.response))
      .subscribe(events => {
        this.events$.next(events);
        this.eventsLoading$.next(false);
      });
  };

  public createEvent = (eventData: {
    eventName: string;
    owner: string;
  }): Observable<any> => {
    return apiService
      .post("/events/", {
        name: eventData.eventName,
        paymaster: { username: eventData.owner }
      })
      .pipe(
        map(ajax => ajax.response),
        tap((event: any) =>
          this.events$.next([...this.events$.getValue(), event])
        )
      );
  };
}

const eventService = new EventService();

export default eventService;
