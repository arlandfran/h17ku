<script>
  import { onMount } from "svelte";
  import { isAuthenticated } from "../stores";
  import tippy from "tippy.js";
  import "tippy.js/dist/tippy.css";
  import "tippy.js/themes/translucent.css";

  onMount(() => {
    if (!$isAuthenticated) {
      tippy("#post", {
        content: "you must be logged in to post haikus",
        arrow: false,
        hideOnClick: false,
        trigger: "mouseenter focus",
        placement: "bottom",
        theme: "translucent",
      });
    }
  });

  async function copy() {
    const text = document.getElementById("haiku-validator");
    await navigator.clipboard.writeText(text.value);
    text.select();
    if (!text.value) {
      text.value += "nothing to copy";
    } else {
      text.value += " - copied";
    }
  }
</script>

<div class="flex gap-4 justify-end dark:text-white">
  {#if $isAuthenticated}
    <button
      class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
      type="submit"
      form="haiku">post</button
    >
  {:else}
    <span
      id="post"
      tabindex="0"
      class="rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
    >
      <button class="p-2 line-through" disabled>post</button>
    </span>
  {/if}

  <button
    id="copy"
    class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
    on:click={copy}>copy</button
  >

  <button
    class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
    >share</button
  >
</div>
