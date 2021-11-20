<script>
  let dark;

  if (
    localStorage.theme === "dark" ||
    (!("theme" in localStorage) &&
      window.matchMedia("(prefers-color-scheme: dark)").matches)
  ) {
    dark = true;
  } else {
    dark = false;
  }

  function toggleIcon() {
    dark = !dark;
  }

  function toggleTheme() {
    document.documentElement.classList.toggle("dark");
    document.getElementById("hamburger").classList.toggle("c-hamburger--light");
  }
</script>

<button
  class="btn hover:bg-gray-400"
  on:click={toggleTheme}
  on:click={toggleIcon}
  aria-label="toggle-theme"
>
  {#if dark}
    <!-- Sun SVG -->
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
  {:else}
    <!-- Moon SVG -->
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
        d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
      />
    </svg>
  {/if}
</button>

<style>
  button {
    transition: background 0.2s ease-in-out;
  }
</style>
