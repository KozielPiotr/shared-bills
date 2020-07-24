/**
 * Events services
 */

import { BehaviorSubject, Observable } from "rxjs";
import { map, tap } from "rxjs/operators";

import apiService, { ApiServiceExact } from "./api";
import { EventInterface } from "../interfaces/interfaces";

/**
 * Manages events
 */
class EventService {
  public events$ = new BehaviorSubject<EventInterface[]>([]);
  public eventUrl$ = new BehaviorSubject<string | null>(null);
  public event$ = new BehaviorSubject<EventInterface | null>(null);
  public eventsLoading$ = new BehaviorSubject<boolean>(false);

  private apiServiceExact = new ApiServiceExact();

  /**
   * Gets all logged user's events
   */
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

  /**
   * Gets a specific event by url
   */
  public fetchEvent = (url: string) => {
    this.apiServiceExact
      .get(url)
      .pipe(map(ajax => ajax.response))
      .subscribe(event => {
        this.event$.next(event);
      });
  };

  /**
   * Gets a specific event by it's ID
   */
  public fetchEventById = (id: string | undefined) => {
    let eventId = id;
    if (!eventId) {
      eventId = "";
    }
    apiService
      .get(`/events/${id}/`)
      .pipe(map(ajax => ajax.response))
      .subscribe(event => {
        this.event$.next(event);
      });
  };

  /**
   * Creates a new event
   */
  public createEvent = (eventData: {
    eventName: string;
    owner: string;
  }): Observable<EventInterface> => {
    return apiService
      .post("/events/", {
        name: eventData.eventName,
        paymaster: { username: eventData.owner }
      })
      .pipe(
        map(ajax => ajax.response),
        tap((event: EventInterface) =>
          this.events$.next([...this.events$.getValue(), event])
        )
      );
  };
}

const eventService = new EventService();

export default eventService;
