<script>
  import { onMount } from "svelte";

  export let showMenu;

  onMount(function checkTheme() {
    if (
      localStorage.theme === "dark" ||
      (!("theme" in localStorage) &&
        window.matchMedia("(prefers-color-scheme: dark)").matches)
    ) {
      document.getElementById("hamburger").classList.add("c-hamburger--light");
    }
  });

  function menuClickHandler() {
    showMenu = !showMenu;
  }
</script>

<button
  class="p-2 md:hidden focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
  on:click={menuClickHandler}
>
  <div
    id="hamburger"
    class="align-middle c-hamburger c-hamburger--chop"
    class:active={showMenu}
  >
    <div class="c-hamburger-inner">
      <span class="c-hamburger-bar" />
      <span class="c-hamburger-bar" />
      <span class="c-hamburger-bar" />
    </div>
  </div>
</button>
