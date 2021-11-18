<script>
  import { ready, url, goto } from "@roxi/routify";
  import { onMount } from "svelte";
  import Post from "../../components/Post.svelte";
  import { isAuthenticated } from "../../stores.js";

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
  {#if $isAuthenticated}
    <h1 class="title">your haikus</h1>
  {:else}
    <h1 class="title">{slug}'s haikus</h1>
  {/if}

  <div class="grid mt-4 w-full max-w-2xl">
    {#each posts as post}
      <Post {...post} />
    {/each}
  </div>
{/if}
