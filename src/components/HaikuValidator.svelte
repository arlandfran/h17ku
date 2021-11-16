<script>
  import { onMount } from "svelte";
  import autosize from "autosize/dist/autosize.min.js";
  import { syllable } from "syllable";

  onMount(() => {
    autosize(document.querySelectorAll("textarea"));
  });

  let text = "";

  $: count = syllable(text);
</script>

<div class="flex flex-col gap-2 w-full max-w-2xl">
  <label for="haiku-validator" class="dark:text-white"
    >compose your haiku:</label
  >

  <textarea
    id="haiku-validator"
    name="haiku-validator"
    class="box-border p-4 w-full rounded border border-black resize-none dark:shadow-lg dark:bg-gray-700 dark:text-white focus:outline-none focus:ring-1 focus:ring-black dark:ring-white dark:border-none dark:focus:ring-2"
    rows="1"
    placeholder="pineapples are good / apples are very yummy / pen is good i guess"
    bind:value={text}
  />

  <div class="dark:text-white">
    syllables: {count}
  </div>
</div>
