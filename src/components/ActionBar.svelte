<script>
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
  <button
    class="p-2 rounded-sm focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
    >post</button
  >
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
