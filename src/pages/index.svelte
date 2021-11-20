<script>
  import { onMount } from "svelte";
  import HaikuValidator from "../components/HaikuValidator.svelte";
  import Post from "../components/post/Post.svelte";
  import PostsFilter from "../components/post/PostsFilter.svelte";
  import { updatePosts, filter, user, isFromRegister } from "../stores";
  import ActionBar from "../components/ActionBar.svelte";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";

  let posts = [];

  getPosts();

  onMount(() => {
    if ($isFromRegister) {
      toast.push("you have been logged in", {
        initial: 1,
        duration: 5000,
        reversed: true,
        dismissable: true,
        intro: { y: 64 },
      });
    }
    $isFromRegister = false;
  });

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
  <h1 class="title">
    haiku<span class="text-rose-500 dark:text-yellow-400">*</span>
  </h1>

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

<div class="flex flex-col gap-y-4 mt-4 w-full max-w-2xl">
  <PostsFilter />

  {#if posts.length}
    {#each posts as post (post._id.$oid)}
      <Post {...post} />
    {/each}
  {/if}
</div>

<Toast />
