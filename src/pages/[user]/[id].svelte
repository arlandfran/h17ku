<script>
  import { params } from "@roxi/routify";
  import { onMount } from "svelte";
  import Post from "../../components/Post.svelte";

  let data;
  let isLoaded = false;

  onMount(async () => {
    const response = await fetch(`/api/post?id=${$params.id}`, {
      credentials: "same-origin",
    });

    const result = await response.json();
    if (response.status === 200) {
      data = await result.data;
      isLoaded = true;
    }
  });
</script>

<div class="grid gap-y-4 w-full max-w-2xl">
  {#if isLoaded}
    <Post {...data} isSelected="true" />
  {/if}
</div>
