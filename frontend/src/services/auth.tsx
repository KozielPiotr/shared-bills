/**
 * Authorisation services
 */
import { Observable, BehaviorSubject } from "rxjs";
import { map, tap } from "rxjs/operators";

import apiService from "./api";
import { localStorageService } from "./storage";

/**
 * Manages authentication
 */
class AuthService {
  private tokenSubject$ = new BehaviorSubject<string | null>(
    localStorageService.getToken()
  );
  private registeredUser$ = new BehaviorSubject<string | null>(null);

  constructor() {
    this.tokenSubject$.subscribe(localStorageService.setToken);
  }

  /**
   * Checks if user is authenticated
   */
  public isAuthenticated(): Observable<boolean> {
    return this.tokenSubject$.pipe(map(token => !!token));
  }

  public justRegistered(): Observable<string | null> {
    return this.registeredUser$.pipe(map(user => user));
  }

  /**
   * Logs user in
   */
  public login = (authData: {
    email: string;
    password: string;
  }): Observable<any> =>
    apiService.post("/token/", authData).pipe(
      map(ajax => ajax.response.access),
      tap(token => this.tokenSubject$.next(token))
    );

  /**
   * Logs user out
   */
  public logout = () => this.tokenSubject$.next(null);

  /**
   * Registers new user
   */
  public register = (registerData: {
    email: string;
    password: string;
  }): Observable<any> =>
    apiService.post("/user/register/", registerData).pipe(
      map(ajax => ajax.response.email),
      tap(user => this.registeredUser$.next(user))
    );
}

const authService = new AuthService();

export default authService;
