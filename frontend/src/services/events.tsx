/**
 * Events services
 */

import { Observable, BehaviorSubject } from "rxjs";
import { map, tap } from "rxjs/operators";

import apiService from "./api";

class EventService {
  private events$ = new BehaviorSubject<any>(
    apiService.get("/events/").pipe(
      map(ajax => ajax.response),
      tap(events => events)
    )
  );

  public getEvents = (): void => {
    this.events$.next(
      apiService.get("/events/").pipe(
        map(ajax => ajax.response),
        tap(events => this.events$.next(events))
      )
    );
  };
  // apiService.get("/events/").pipe(
  //   map(ajax => ajax.response),
  //   tap(events => this.events$.next(events))
  // );

  public events(): Observable<any> {
    return this.events$;
  }
}

const eventService = new EventService();

export default eventService;
