/**
 * Payments serices
 */

import { BehaviorSubject } from "rxjs";
import { map } from "rxjs/operators";

import { ApiServiceExact } from "./api";
import { PaymentInterface } from "../interfaces/interfaces";

/**
 * Manages event's payments
 */
class PaymentsService {
  public payments$ = new BehaviorSubject<PaymentInterface[] | null>(null);

  private apiServiceExact = new ApiServiceExact();

  /**
   * Gets all payments related to the event
   */
  public fetchPayments = (url: string) => {
    this.apiServiceExact
      .get(url)
      .pipe(map(ajax => ajax.response))
      .subscribe(payments => {
        this.payments$.next(payments);
      });
  };
}

const paymentsService = new PaymentsService();

export default paymentsService;
