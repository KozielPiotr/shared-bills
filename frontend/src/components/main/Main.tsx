/**
 * Main page
 */

import React from "react";

import authService from "../../services/auth";

/**
 * Main component for main page
 */
function MainPage() {
  return (
    <div>
      <p>
        <button onClick={authService.logout}>Logout</button>
      </p>
    </div>
  );
}

export default MainPage;
