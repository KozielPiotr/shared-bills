/**
 * Bills serices
 */

import { BehaviorSubject, Observable } from "rxjs";
import { map } from "rxjs/operators";

import { ApiServiceExact } from "./api";
import { BillInterface } from "../interfaces/interfaces";

/**
 * Manages event's bills
 */
class BillsService {
  public bills$ = new BehaviorSubject<BillInterface[] | null>(null);
  public bill$ = new BehaviorSubject<BillInterface | null>(null);
  public updatedBill$ = new BehaviorSubject<BillInterface | null>(null);

  private apiServiceExact = new ApiServiceExact();

  /**
   * Gets all bills related to the event
   */
  public fetchBills = (url: string) => {
    this.apiServiceExact
      .get(url)
      .pipe(map(ajax => ajax.response))
      .subscribe(bills => {
        this.bills$.next(bills);
      });
  };

  /**
   * Gets bill object data
   */
  public fetchBill = (billUrl: string) => {
    this.apiServiceExact
      .get(billUrl)
      .pipe(map(ajax => ajax.response))
      .subscribe(bill => {
        this.bill$.next(bill);
      });
  };

  /**
   * Updats bill object
   */
  public updateBill = (
    url: string,
    billData: BillInterface
  ): Observable<BillInterface> => {
    return this.apiServiceExact
      .patch(url, billData)
      .pipe(map(ajax => ajax.response));
  };
}

const billsService = new BillsService();

export default billsService;
