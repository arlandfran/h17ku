<script>
  import ThemeToggler from "../components/ThemeToggle.svelte";
  import Hamburger from "../components/Hamburger.svelte";
  import { fade, slide } from "svelte/transition";
  import { media } from "svelte-match-media";
  import { isAuthenticated, user } from "../stores";

  let showMenu = false;

  const unprotectedPages = [
    { link: "home", href: "./" },
    { link: "log in", href: "./login" },
    { link: "register", href: "./register" },
  ];

  const protectedPages = [
    { link: "home", href: "./" },
    { link: "account", href: `./[user]` },
  ];

  $: if ($media.desktop) {
    showMenu = false;
  }

  function logout() {
    fetch("/api/auth/logout", {
      credentials: "same-origin",
    })
      .then((response) => response.json())
      .then((result) => {
        if (result.logout) {
          $isAuthenticated = false;
        }
      })
      .catch((err) => {
        console.log(err);
      });
  }
</script>

<header class="flex justify-center w-full">
  <div class="flex flex-col items-end p-4 md:py-4 md:px-0 w-192 min-h-16">
    <div class="flex gap-x-4 items-center">
      <ThemeToggler />
      <Hamburger bind:showMenu />
      <nav class="hidden md:block">
        {#if $isAuthenticated}
          <ul class="flex gap-2 items-center">
            {#each protectedPages as { link, href }}
              <li>
                <a
                  class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
                  {href}>{link}</a
                >
              </li>
            {/each}
            <button
              class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
              on:click={logout}>logout</button
            >
          </ul>
        {:else}
          <ul class="flex gap-2">
            {#each unprotectedPages as { link, href }}
              <li
                class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
              >
                <a {href}>{link}</a>
              </li>
            {/each}
          </ul>
        {/if}
      </nav>
    </div>
    {#if showMenu}
      <nav
        class="flex justify-end pt-4 w-full max-w-7xl text-right"
        transition:slide={{ duration: 200 }}
      >
        {#if $isAuthenticated}
          <ul class="flex flex-col gap-4" in:fade>
            {#each protectedPages as { link, href }}
              <li>
                <a
                  class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
                  {href}>{link}</a
                >
              </li>
            {/each}
            <button
              class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
              on:click={logout}>logout</button
            >
          </ul>
        {:else}
          <ul class="flex flex-col" in:fade>
            {#each unprotectedPages as { link, href }}
              <li
                class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
              >
                <a {href}>{link}</a>
              </li>
            {/each}
          </ul>
        {/if}
      </nav>
    {/if}
  </div>
</header>
