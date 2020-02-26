/**
 * Main page
 */

import React from "react";

import { Observable } from "rxjs";

import authService from "../../services/auth";

/**
 * Main component for main page
 */
function MainPage() {
  const useObservable = (observable: Observable<boolean>) => {
    const [state, setState] = React.useState();

    React.useEffect(() => {
      const sub = observable.subscribe(setState);
      return () => sub.unsubscribe();
      // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return state;
  };

  const isAuthenticated = useObservable(authService.isAuthenticated());

  return (
    <div>
      <p>
        <button onClick={authService.logout}>Logout</button>
      </p>
    </div>
  );
}

export default MainPage;
