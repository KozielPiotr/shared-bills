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

  constructor() {
    this.tokenSubject$.subscribe(localStorageService.setToken);
  }

  /**
   * Checks if user is authenticated
   */
  public isAuthenticated(): Observable<boolean> {
    return this.tokenSubject$.pipe(map(token => !!token));
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
}

const authService = new AuthService();

export default authService;
