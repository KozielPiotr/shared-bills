/**
 * interfaces used across whole app
 */

export interface ParticipantInterface {
  id: number;
  url: string;
  username: string;
}

export interface BillInterface {
  id: number;
  url: string;
  participants: number[];
  title: string;
  amount_currency: string;
  amount: string;
  event: number;
  payer: number;
}

export interface PaymentInterface {
  id: number;
  url: string;
  issuer: number;
  acquirer: number;
  title: string;
  amount_currency: string;
  amount: string;
  event: number;
}

export interface EventInterface {
  id: number;
  paymaster: ParticipantInterface;
  url: string;
  participants_url: string;
  bills_url: string;
  payments_url: string;
  participants: ParticipantInterface[];
  bills: BillInterface[];
  payments: PaymentInterface[];
  name: string;
}
