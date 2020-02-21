import React from "react";

import authService from "../services/auth";

function App() {
  const [isAuthenticated, setAuthenticated] = React.useState<boolean>(false);

  React.useEffect(() => {
    const subscription = authService
      .isAuthenticated()
      .subscribe(setAuthenticated);
    return () => subscription.unsubscribe();
  }, []);

  return (
    <div className="App">{isAuthenticated ? "Hello" : "Unauthorized"}</div>
  );
}

export default App;
