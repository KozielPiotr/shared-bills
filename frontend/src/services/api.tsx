import { Observable } from "rxjs";
import { ajax, AjaxResponse } from "rxjs/ajax";
import urljoin from "url-join";

class ApiService {
  private apiUrl = "http://localhost:8000/api/";

  public get = (url: string): Observable<AjaxResponse> => this.call("GET", url);

  public post = (url: string, body?: any): Observable<AjaxResponse> =>
    this.call("POST", url, body);

  public put = (url: string, body?: any): Observable<AjaxResponse> =>
    this.call("PUT", url, body);

  public patch = (url: string, body?: any): Observable<AjaxResponse> =>
    this.call("PATCH", url, body);

  public delete = (url: string): Observable<AjaxResponse> =>
    this.call("DELETE", url);

  private call = (
    method: string,
    url: string,
    body?: any
  ): Observable<AjaxResponse> =>
    ajax({
      method,
      url: urljoin(this.apiUrl, url),
      headers: { "Content-Type": "application/json" },
      body
    });
}

const apiService = new ApiService();

export default apiService;
