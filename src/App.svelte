<script>
  import { Router, ready, beforeUrlChange } from "@roxi/routify";
  import { routes } from "../.routify/routes";
  import { isAuthenticated, user, csrf, filter } from "./stores";

  getCSRF();
  getSession();

  $beforeUrlChange(() => {
    getSession();
    return true;
  });

  async function getSession() {
    const response = await fetch("/api/auth/session", {
      credentials: "same-origin",
    });
    const result = await response.json();
    if (result.login) {
      $isAuthenticated = result.login;
      $user = result.id;
      $filter = "my haikus";
    }
  }

  function getCSRF() {
    $csrf = document.getElementsByName("csrf-token")[0].content;
  }
</script>

<Router {routes} />
