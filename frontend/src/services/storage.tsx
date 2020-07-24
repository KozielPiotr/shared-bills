/**
 * Manages browser storages
 */

/**
 * Manages local storage
 */
class LocalStorageService {
  /**
   * Gets token from local storage
   */
  public getToken(): string | null {
    return localStorage.getItem("token");
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

  /**
   * Sets eventUrl to local storage to prevent data when event page is refreshed
   * @param {string} url - url to get event data from api
   */
  public setEventUrl(url: string) {
    url
      ? localStorage.setItem("eventUrl", url)
      : localStorage.removeItem("eventUrl");
  }

  /**
   * Gets url of the event from local storage
   */
  public getEventUrl(): string {
    const url = localStorage.getItem("eventUrl");
    if (url) {
      return url;
    } else return "";
  }
}

export const localStorageService = new LocalStorageService();
