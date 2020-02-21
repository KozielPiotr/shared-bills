import { Observable, BehaviorSubject } from "rxjs";
import { map } from "rxjs/operators";

class AuthService {
  private tokenSubject = new BehaviorSubject<string | null>(null);

  public isAuthenticated(): Observable<boolean> {
    return this.tokenSubject.pipe(map(token => !!token));
  }
}

const authService = new AuthService();

export default authService;
