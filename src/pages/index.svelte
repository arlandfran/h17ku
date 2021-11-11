<script>
  import { onMount } from "svelte";
  import { isAuthenticated } from "../stores";

  let id;

  onMount(() => {
    fetch("/api/auth/session", {
      credentials: "same-origin",
    })
      .then((res) => res.json())
      .then((data) => {
        if (data.login) {
          $isAuthenticated = true;
          id = data.id;
        }
      });
  });
</script>

<h1 class="text-4xl font-bold dark:text-white">haiku*</h1>

<p class="dark:text-white">authenticated: {$isAuthenticated}</p>

{#if $isAuthenticated}
  <p class="dark:text-white">id: {id}</p>
{/if}
