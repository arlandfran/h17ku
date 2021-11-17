<script>
  import Post from "../components/Post.svelte";

  export let posts;
</script>

<div class="grid max-w-4xl sm:grid-cols-2 md:gap-x-8 >">
  {#each posts as post}
    <Post {...post} />
  {/each}
</div>
