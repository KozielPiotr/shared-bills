/**
 * Commonly used hooks
 */

import React from "react";

import { Observable } from "rxjs";

/**
 * hooks that are used repeatedly
 */
class HooksService {
  /**
   * changes state based on observable
   */
  public useObservable = (observable: Observable<boolean>) => {
    const [state, setState] = React.useState();

    React.useEffect(() => {
      const sub = observable.subscribe(setState);
      return () => sub.unsubscribe();
      // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    return state;
  };
}

export const hookService = new HooksService();
