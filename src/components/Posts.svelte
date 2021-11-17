<script>
  import Post from "../components/Post.svelte";

  export let posts;
</script>

<div
  class="grid gap-4 max-w-4xl sm:grid-cols-2 md:gap-x-8 md:gap-x-316> md:gap-y-16"
>
  {#each posts as post}
    <Post {...post} />
  {/each}
</div>
