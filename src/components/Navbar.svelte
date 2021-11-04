<script>
  import ThemeToggler from "../components/ThemeToggle.svelte";
  import Hamburger from "../components/Hamburger.svelte";
  import { fade, slide } from "svelte/transition";
  import { media } from "svelte-match-media";

  let showMenu = false;

  const navLinks = [
    { link: "Log in", href: "./login" },
    { link: "Register", href: "./register" },
  ];

  $: if ($media.desktop) {
    showMenu = false;
  }
</script>

<header
  class="flex flex-col justify-center items-end p-4 w-full max-w-7xl min-h-16"
>
  <div class="flex gap-4 items-center">
    <ThemeToggler />

    <Hamburger bind:showMenu />

    <nav class="hidden md:block">
      <ul class="flex gap-2">
        {#each navLinks as { link, href }}
          <li>
            <a class="p-2" {href}>{link}</a>
          </li>
        {/each}
      </ul>
    </nav>
  </div>

  {#if showMenu}
    <nav
      class="flex justify-end pt-4 w-full max-w-7xl text-right"
      transition:slide={{ duration: 200 }}
    >
      <ul class="flex flex-col gap-4" in:fade>
        {#each navLinks as { link, href }}
          <li>
            <a class="p-2" {href}>{link}</a>
          </li>
        {/each}
      </ul>
    </nav>
  {/if}
</header>
