/**
 * Utilities for Participants component
 */

import {
  BillInterface,
  PaymentInterface
} from "../../../../../interfaces/interfaces";

/**
 * Counts number of the participant's bills
 */
export function countBills(bills: BillInterface[], participantId: number) {
  let billsNumber = 0;

  if (bills != null) {
    for (let bill of bills) {
      const participants = bill.participants;
      for (let i = 0; i < participants.length; ++i) {
        participants[i] === participantId && billsNumber++;
      }
    }
  }
  return billsNumber;
}

/**
 * Counts number of the participant's payments (as acquirer)
 */
export function countPaymentsAcquirer(
  payments: PaymentInterface[],
  participantId: number
) {
  let paymentsNumber = 0;

  if (payments != null) {
    for (let payment of payments) {
      payment.acquirer === participantId && paymentsNumber++;
    }
  }
  return paymentsNumber;
}

/**
 * Counts number of the participant's payments (as issuer)
 */
export function countPaymentsIssuer(
  payments: PaymentInterface[],
  participantId: number
) {
  let paymentsNumber = 0;

  if (payments != null) {
    for (let payment of payments) {
      payment.issuer === participantId && paymentsNumber++;
    }
  }
  return paymentsNumber;
}
