import { localStorageService } from "./storage"


class ApiService {
  private apiUrl = "http://localhost:8000/api/"
  
  public login(email: string, password: string) {
    return (async() => {
      const response = await fetch(
        `${this.apiUrl}token/`, {
          method: "POST",
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({email, password})
        }
      )
      const token = await response.json()
      localStorageService.setToken(token["access"])
    })()
  }

  public logout() {
  localStorageService.setToken(null)
  }
}



const apiService = new ApiService();

export default apiService
