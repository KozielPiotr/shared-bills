/**
 * Manages browser storages
 */

/**
 * Manages local storage
 */
class LocalStorageService {
  tokenKey = "token";

  /**
   * Gets token from local storage
   */
  public getToken(): string | null {
    return localStorage.getItem(this.tokenKey);
  }

  /**
   * Sets token value in local storage
   * @param {string} token - access or refresh token for api
   */
  public setToken(token: string | null) {
    token
      ? localStorage.setItem("token", token)
      : localStorage.removeItem("token");
  }
}

export const localStorageService = new LocalStorageService();
