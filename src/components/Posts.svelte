<script>
  import Post from "../components/Post.svelte";
  import PostsFilter from "../components/PostsFilter.svelte";

  export let posts = [];
</script>

<div class="grid w-full max-w-2xl">
  <PostsFilter />
  {#each posts as post}
    <Post {...post} />
  {/each}
</div>
