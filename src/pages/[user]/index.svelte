<script>
  import { ready, url, goto } from "@roxi/routify";
  import { onMount } from "svelte";
  import Post from "../../components/Post.svelte";

  let posts = [];
  const slug = $url().slice(1);
  let user = false;

  onMount(async () => {
    const response = await fetch(`/api/user?username=${slug}`, {
      credentials: "same-origin",
    });
    const result = await response.json();

    if (response.status === 200) {
      posts = result.data;
      user = true;
      $ready();
    } else if (response.status === 404) {
      $goto("../404", {}, true);
    }
  });
</script>

{#if user}
  <h1 class="mb-4 text-4xl font-bold dark:text-white">your haikus</h1>

  <div class="max-w-2xl gridw-full">
    {#each posts as post}
      <Post {...post} />
    {/each}
  </div>
{/if}
