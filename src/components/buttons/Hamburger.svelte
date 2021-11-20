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

<button class="btn md:hidden" on:click={menuClickHandler} aria-label="open-menu">
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
