<script>
  import HaikuValidator from "../components/HaikuValidator.svelte";
  import Post from "../components/Post.svelte";
  import PostsFilter from "../components/PostsFilter.svelte";
  import { updatePosts, filter, user } from "../stores";
  import ActionBar from "../components/ActionBar.svelte";

  let posts = [];

  getPosts();

  async function getPosts() {
    if ($filter === "my-haikus") {
      const response = await fetch(
        `/api/posts?filter=my-haikus&username=${$user}`,
        {
          credentials: "same-origin",
        }
      );
      const result = await response.json();
      posts = result.data;
    } else {
      const response = await fetch(`/api/posts?filter=${$filter}`, {
        credentials: "same-origin",
      });
      const result = await response.json();
      posts = result.data;
    }
  }

  $: if ($updatePosts) {
    getPosts();
    $updatePosts = false;
  }
</script>

<section class="mb-4 w-full max-w-2xl">
  <h1 class="title">haiku<span class="text-yellow-400">*</span></h1>

  <p>
    *a form of japanese poetry - a haiku expresses a single feeling or
    impression and contains three unrhymed lines of five, seven, and five
    syllables, respectively.
  </p>
</section>

<HaikuValidator />

<div
  class="pb-4 w-full max-w-2xl text-right border-b border-black dark:border-gray-400"
>
  <ActionBar />
</div>

<div class="flex flex-col gap-y-4 mt-2 w-full max-w-2xl">
  <PostsFilter />

  {#if posts.length}
    {#each posts as post}
      <Post {...post} />
    {/each}
  {/if}
</div>
