/**
 * Main page
 */

import React from "react";

import { Observable } from "rxjs";

import authService from "../../services/auth";
import apiService from "../../services/api"


/**
 * Main component for main page
 */
function MainPage() {

  const useObservable = (observable: Observable<boolean>) => {
    const [state, setState] = React.useState();
  
    React.useEffect(() => {
      const sub = observable.subscribe(setState);
      return () => sub.unsubscribe();
    }, []);
  
    return state;
  };

  const isAuthenticated = useObservable(authService.isAuthenticated())

  const handleLogin = () => {
    apiService.login("admin@admin.com", "a")
  }

  const handleLogout = () => {
    apiService.logout()
  }

  return (
    <div>
      <p>{isAuthenticated ? "Hello" : "Unauthorized"}</p>
      <p>{localStorage.getItem("token")}</p>
      <p><button onClick={handleLogin}>Login</button></p>
      <p><button onClick={handleLogout}>Logout</button></p>
    </div>

  );
}

export default MainPage;