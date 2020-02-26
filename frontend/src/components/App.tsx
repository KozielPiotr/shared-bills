import React from "react";
import {
	BrowserRouter as Router,
	Route,
} from "react-router-dom"
import { Observable } from "rxjs";

import authService from "../services/auth";
// import apiService from "../services/api"
import LoginPage from "./login/Login"


/**
 * Main application function
 */
function App() {

  const useObservable = (observable: Observable<boolean>) => {
    const [state, setState] = React.useState();
  
    React.useEffect(() => {
      const sub = observable.subscribe(setState);
      return () => sub.unsubscribe();
    }, []);
  
    return state;
  };

  const isAuthenticated = useObservable(authService.isAuthenticated())

  // const handleLogin = () => {
  //   apiService.login("admin@admin.com", "a")
  // }

  // const handleLogout = () => {
  //   apiService.logout()
  // }

  return (
    // <div className="App">
    //   <p>{isAuthenticated ? "Hello" : "Unauthorized"}</p>
    //   <p>{localStorage.getItem("token")}</p>
    //   <p><button onClick={handleLogin}>Login</button></p>
    //   <p><button onClick={handleLogout}>Logout</button></p>
    // </div>
    <Router>
			<Route exact path="/login" component={LoginPage} />
		</Router>
  );
}

export default App;
