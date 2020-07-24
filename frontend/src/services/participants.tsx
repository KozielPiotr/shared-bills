/**
 * Participants serices
 */

import { BehaviorSubject, Observable } from "rxjs";
import { map, tap } from "rxjs/operators";

import apiService, { ApiServiceExact } from "./api";
import { ParticipantInterface } from "../interfaces/interfaces";

/**
 * Manages events's participants
 */
class ParticipantService {
  public participants$ = new BehaviorSubject<ParticipantInterface[]>([]);
  public participant$ = new BehaviorSubject<ParticipantInterface | null>(null);

  private apiServiceExact = new ApiServiceExact();

  /**
   * Gets all participants data
   */
  public fetchParticipants = (url: string) => {
    this.apiServiceExact
      .get(url)
      .pipe(map(ajax => ajax.response))
      .subscribe(participants => {
        this.participants$.next(participants);
      });
  };

  /**
   * Gets a participant data by participant's ID
   */
  public fetchParticipantById = (eventId: number, participantId: number) => {
    apiService
      .get(`/events/${eventId}/participants/${participantId}/`)
      .pipe(map(ajax => ajax.response))
      .subscribe(participant => {
        this.participant$.next(participant);
      });
  };

  /**
   * Creates a new participant
   */
  public createParticipant = (
    participantData: {
      participantName: string;
    },
    eventId: number
  ): Observable<ParticipantInterface> => {
    return apiService
      .post(`/events/${eventId}/participants/`, {
        username: participantData.participantName
      })
      .pipe(
        map(ajax => ajax.response),
        tap((participant: ParticipantInterface) =>
          this.participants$.next([
            ...this.participants$.getValue(),
            participant
          ])
        )
      );
  };

  /**
   * Deletes the participant
   */
  public deleteParticipant = (
    url: string
  ): Observable<ParticipantInterface> => {
    return this.apiServiceExact.delete(url).pipe(
      map(ajax => ajax.response),
      tap(error => error)
    );
  };
}

const participantService = new ParticipantService();

export default participantService;
