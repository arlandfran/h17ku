<script>
  import { Router, ready, beforeUrlChange } from "@roxi/routify";
  import { routes } from "../.routify/routes";
  import { isAuthenticated, user, csrf } from "./stores";

  getCSRF();
  getSession();

  $beforeUrlChange(() => {
    getSession();
    return true;
  });

  async function getSession() {
    const res = await fetch("/api/auth/session", {
      credentials: "same-origin",
    });
    const result = await res.json();
    $isAuthenticated = result.login;
    $user = result.id;
    $ready();
  }

  function getCSRF() {
    $csrf = document.getElementsByName("csrf-token")[0].content;
  }
</script>

<Router {routes} />
