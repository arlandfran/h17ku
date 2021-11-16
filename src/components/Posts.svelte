<script>
  export let posts;

  import Post from "../components/Post.svelte";
</script>

<div class="grid gap-4 max-w-2xl sm:grid-cols-2 xl:grid-cols-3 xl:gap-16">
  {#each posts as post}
    <Post {...post} />
  {/each}
</div>
