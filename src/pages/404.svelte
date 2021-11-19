<script>
  import { onMount } from "svelte";
  import { ready } from "@roxi/routify";

  let haiku = false;
  let error;

  onMount(async () => {
    const response = await fetch("/api/haiku?type=error", {
      credentials: "same-origin",
    });
    const result = await response.json();
    error = result.data;
    haiku = true;
    $ready();
  });
</script>

{#if haiku}
  <div class="flex justify-center items-center w-screen vh-6">
    <div class="text-center">
      <h1 class="mb-4 text-2xl font-bold whitespace-pre-line">{error}</h1>
      <a href="/" class="">Go back</a>
    </div>
  </div>
{/if}

<style>
  .vh-6 {
    height: 60vh;
  }
</style>
