/**
 * Interfaces used in login
 */

/**
 * Interface used in login form
 */
export interface AuthState {
  email: string;
  password: string;
}

/**
 * Interface used in email field in login form
 */
export interface EmailFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  email: string;
  error: boolean;
}

/**
 * Interface used in password field in login form
 */
export interface PasswordFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  password: string;
  error: boolean;
}
