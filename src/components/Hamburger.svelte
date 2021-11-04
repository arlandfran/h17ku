<script>
  export let showMenu;

  function menuClickHandler() {
    showMenu = !showMenu;
  }
</script>

<button
  class="p-2 md:hidden focus:outline-none focus:ring-2 focus:ring-black"
  on:click={menuClickHandler}
>
  <div
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
