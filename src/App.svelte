<script>
  import { Router, ready, beforeUrlChange } from "@roxi/routify";
  import { routes } from "../.routify/routes";
  import { isAuthenticated } from "./stores";

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
    $ready();
  }
</script>

<Router {routes} />
