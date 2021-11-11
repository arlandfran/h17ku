<script>
  import ThemeToggler from "../components/ThemeToggle.svelte";
  import Hamburger from "../components/Hamburger.svelte";
  import { fade, slide } from "svelte/transition";
  import { media } from "svelte-match-media";
  import { isAuthenticated } from "../stores";

  let showMenu = false;

  const defaultLinks = [
    { link: "log in", href: "./login" },
    { link: "register", href: "./register" },
  ];

  $: if ($media.desktop) {
    showMenu = false;
  }

  function logout() {
    fetch("/api/auth/logout", {
      credentials: "same-origin",
    })
      .then(() => {
        $isAuthenticated = false;
      })
      .catch((err) => {
        console.log(err);
      });
  }
</script>

<header
  class="flex flex-col justify-center items-end p-4 w-full max-w-7xl min-h-16 dark:text-white"
>
  <div class="flex gap-4 items-center">
    <ThemeToggler />

    <Hamburger bind:showMenu />

    <nav class="hidden md:block">
      {#if $isAuthenticated}
        <ul class="flex gap-2">
          <button
            class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
            on:click={logout}>logout</button
          >
        </ul>
      {:else}
        <ul class="flex gap-2">
          {#each defaultLinks as { link, href }}
            <li>
              <a
                class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
                {href}>{link}</a
              >
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
          <button
            class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
            on:click={logout}>logout</button
          >
        </ul>
      {:else}
        <ul class="flex flex-col gap-4" in:fade>
          {#each defaultLinks as { link, href }}
            <li>
              <a
                class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
                {href}>{link}</a
              >
            </li>
          {/each}
        </ul>
      {/if}
    </nav>
  {/if}
</header>
