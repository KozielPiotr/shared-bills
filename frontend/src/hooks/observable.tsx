import React from "react";

import { Observable } from "rxjs";

/**
 * Changes state based on given observable
 *
 * @param {Observable} observable - Observable used to change state
 */
function useObservable(observable: Observable<boolean | string | null>) {
  const [state, setState] = React.useState();

  React.useEffect(() => {
    const sub = observable.subscribe(setState);
    return () => sub.unsubscribe();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return state;
}

export default useObservable;
