import { Observable, BehaviorSubject } from "rxjs";
import { map, tap } from "rxjs/operators";

import apiService from "./api";
import { localStorageService } from "./storage";

class AuthService {
  private tokenSubject$ = new BehaviorSubject<string | null>(
    localStorageService.getToken()
  );

  constructor() {
    this.tokenSubject$.subscribe(localStorageService.setToken);
  }

  public isAuthenticated(): Observable<boolean> {
    return this.tokenSubject$.pipe(map(token => !!token));
  }

  public login = (authData: {
    email: string;
    password: string;
  }): Observable<any> =>
    apiService.post("/token/", authData).pipe(
      map(ajax => ajax.response.access),
      tap(token => this.tokenSubject$.next(token))
    );

  public logout = () => this.tokenSubject$.next(null);
}

const authService = new AuthService();

export default authService;
