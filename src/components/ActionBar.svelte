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

<div class="flex gap-4 justify-end">
  <span id="post" class="btn" tabindex="0">
    <button
      class="disabled:line-through disabled:cursor-default"
      disabled={!$isAuthenticated}
      tabindex="-1"
      type="submit"
      form="haiku">post</button
    >
  </span>

  <button class="btn" id="copy" on:click={copy}>copy</button>

  <button class="btn">share</button>
</div>
