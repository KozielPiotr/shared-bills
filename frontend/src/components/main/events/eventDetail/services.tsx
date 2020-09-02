/**
 * Service to manage including participants to the bill
 */

import { BehaviorSubject } from "rxjs";

import { ParticipantInterface } from "../../../../interfaces/interfaces";

/**
 * Observables to manage participants inside detailed wiev
 */
class SelectParticipantsService {
  public included$ = new BehaviorSubject<ParticipantInterface[]>([]);

  /**
   * Sets the array of selected participants
   */
  public setIncluded = (included: ParticipantInterface[]) => {
    this.included$.next(included);
  };
}

const selectParticipantsService = new SelectParticipantsService();

export default selectParticipantsService;
