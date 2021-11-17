<script>
  import { ready, url, goto } from "@roxi/routify";
  import { onMount } from "svelte";
  import Posts from "../components/Posts.svelte";

  let posts = [];
  const slug = $url().slice(1);
  let user = false;

  onMount(async () => {
    const response = await fetch(`/api/user?username=${slug}`);
    const result = await response.json();

    if (response.status === 200) {
      posts = result.data;
      user = true;
      $ready();
    } else if (response.status === 404) {
      $goto("../404", {}, true);
      console.log("not found");
    }
  });
</script>

{#if user}
  <h1 class="mb-4 text-4xl font-bold dark:text-white">{slug}</h1>

  <Posts {posts} />
{/if}
