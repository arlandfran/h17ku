<script>
  import ThemeToggler from "../buttons/ThemeToggle.svelte";
  import Hamburger from "../buttons/Hamburger.svelte";
  import { fade, slide } from "svelte/transition";
  import { media } from "svelte-match-media";
  import { isAuthenticated, user } from "../../stores";
  import { url, isActive } from "@roxi/routify";

  let showMenu = false;

  const unprotectedPages = [
    { link: "home", href: "/index" },
    { link: "log in", href: "/login" },
    { link: "register", href: "/register" },
  ];

  const protectedPages = [
    { link: "home", href: "/index" },
    { link: "account", href: $url(`/${$user}`) },
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

<header class="flex justify-end p-4 w-full">
  <div class="flex flex-col items-end min-h-16">
    <div class="flex gap-x-4 items-center">
      <ThemeToggler />
      <Hamburger bind:showMenu />
      <nav class="hidden gap-x-2 md:flex">
        {#if $isAuthenticated}
          <ul class="flex gap-x-2 items-center">
            {#each protectedPages as { link, href }}
              <li>
                <a class="link" {href} class:active={$isActive(href)}>{link}</a>
              </li>
            {/each}
          </ul>
          <button class="btn" on:click={logout}>logout</button>
        {:else}
          <ul class="flex gap-2">
            {#each unprotectedPages as { link, href }}
              <li>
                <a class="link" {href} class:active={$isActive(href)}>{link}</a>
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
          <ul class="flex flex-col gap-y-4" in:fade>
            {#each protectedPages as { link, href }}
              <li>
                <a class="link" {href} class:active={$isActive(href)}
                  >{link}
                </a>
              </li>
            {/each}
            <button on:click={logout}>logout</button>
          </ul>
        {:else}
          <ul class="flex flex-col gap-y-4" in:fade>
            {#each unprotectedPages as { link, href }}
              <li>
                <a class="link" {href} class:active={$isActive(href)}>{link}</a>
              </li>
            {/each}
          </ul>
        {/if}
      </nav>
    {/if}
  </div>
</header>
