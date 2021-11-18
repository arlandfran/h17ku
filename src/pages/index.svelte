<script>
  import HaikuValidator from "../components/HaikuValidator.svelte";
  import Post from "../components/Post.svelte";
  import PostsFilter from "../components/PostsFilter.svelte";
  import { updatePosts, filter, user } from "../stores";

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
  <h1 class="title">haiku*</h1>

  <p>
    *a form of japanese poetry - a haiku expresses a single feeling or
    impression and contains three unrhymed lines of five, seven, and five
    syllables, respectively.
  </p>
</section>

<HaikuValidator />

<div class="flex flex-col gap-y-4 w-full max-w-2xl">
  <PostsFilter />

  {#each posts as post}
    <Post {...post} />
  {/each}
</div>
