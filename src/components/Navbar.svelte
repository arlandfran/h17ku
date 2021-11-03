<script>
  import { slide } from "svelte/transition";
  import { media } from "svelte-match-media";

  let showMenu = false;

  const navLinks = [
    { link: "Log in", href: "./login" },
    { link: "Register", href: "./register" },
  ];

  function menuClickHandler() {
    showMenu = !showMenu;
  }

  $: if ($media.desktop) {
    showMenu = false;
  }
</script>

<header class="flex gap-4 justify-end items-center p-4 w-full max-w-7xl h-16">
  <!-- Theme toggler -->
  <button class="p-2">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="w-6 h-6"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"
      />
    </svg>
  </button>

  <!-- Hamburger -->
  <button class="p-2 md:hidden" on:click={menuClickHandler}>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="w-6 h-6"
      fill="none"
      viewBox="0 0 24 24"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M4 6h16M4 12h16M4 18h16"
      />
    </svg>
  </button>

  <nav class="hidden md:block">
    <ul class="flex gap-2">
      {#each navLinks as { link, href }}
        <li>
          <a class="p-2" {href}>{link}</a>
        </li>
      {/each}
    </ul>
  </nav>
</header>

{#if showMenu}
  <nav
    class="flex justify-end px-4 w-full max-w-7xl text-right"
    transition:slide={{ duration: 200 }}
  >
    <ul class="flex flex-col gap-4">
      {#each navLinks as { link, href }}
        <li>
          <a class="p-2" {href}>{link}</a>
        </li>
      {/each}
    </ul>
  </nav>
{/if}
