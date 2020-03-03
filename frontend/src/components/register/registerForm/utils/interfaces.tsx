/**
 * Interfaces used in registration
 */

/**
 * Interface used in registration form
 */
export interface RegisterState {
  email: string;
  password: string;
  password2: string;
}

/**
 * Interface used in email field in registration form
 */
export interface EmailFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  email: string;
  error: boolean;
}

/**
 * Interface used in password field in registration form
 */
export interface PasswordFieldProps {
  handleChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  id: string;
  password: string;
  error: boolean;
}

export interface SuccessProps {
  registeredUser: string;
}
