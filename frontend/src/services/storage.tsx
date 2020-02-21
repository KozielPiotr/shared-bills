class LocalStorageService {
  tokenKey = "token";

  public getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  public setToken(token: string | null) {
    token
      ? localStorage.setItem("token", token)
      : localStorage.removeItem("token");
  }
}

export const localStorageService = new LocalStorageService();
