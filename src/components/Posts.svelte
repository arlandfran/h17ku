<script>
  import Post from "../components/Post.svelte";

  export let posts;
</script>

<div class="grid max-w-4xl">
  {#each posts as post}
    <Post {...post} />
  {/each}
</div>
