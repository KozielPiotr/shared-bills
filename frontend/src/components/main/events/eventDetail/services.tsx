/**
 * Service to manage including participants to the bill
 */

import { BehaviorSubject } from "rxjs";

import { ParticipantInterface } from "../../../../interfaces/interfaces";

class SelectParticipantsService {
  public included$ = new BehaviorSubject<ParticipantInterface[]>([]);

  public setIncluded = (included: ParticipantInterface[]) => {
    this.included$.next(included);
  };
}

const selectParticipantsService = new SelectParticipantsService();

export default selectParticipantsService;
