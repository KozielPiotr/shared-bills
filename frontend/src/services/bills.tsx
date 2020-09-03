/**
 * Bills serices
 */

import { BehaviorSubject, Observable } from "rxjs";
import { map, tap } from "rxjs/operators";

import apiService, { ApiServiceExact } from "./api";
import { BillInterface } from "../interfaces/interfaces";

/**
 * Manages event's bills
 */
class BillsService {
  public bills$ = new BehaviorSubject<BillInterface[]>([]);
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
   * Gets bill object data and passes it to given subject
   */
  public fetchBillToObject = (
    billUrl: string,
    obj: BehaviorSubject<BillInterface | null>
  ) => {
    this.apiServiceExact
      .get(billUrl)
      .pipe(map(ajax => ajax.response))
      .subscribe(bill => {
        obj.next(bill);
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

  public createBill = (
    eventId: number,
    billData: {
      title: string;
      amount: string;
      participants: number[];
      payer: number;
    }
  ): Observable<BillInterface> => {
    return apiService
      .post(`/events/${eventId}/bills/`, {
        participants: billData.participants,
        title: billData.title,
        amount: billData.amount,
        payer: billData.payer
      })
      .pipe(
        map(ajax => ajax.response),
        tap((bill: BillInterface) =>
          this.bills$.next([...this.bills$.getValue(), bill])
        )
      );
  };
}

const billsService = new BillsService();

export default billsService;
