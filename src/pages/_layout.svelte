<!-- routify:options preload="proximity" -->
<script>
  import Navbar from "../components/layout/Navbar.svelte";
</script>

<Navbar />

<main class="flex flex-col items-center p-4">
  <slot />
</main>
