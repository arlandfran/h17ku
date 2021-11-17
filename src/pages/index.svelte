<script>
  import HaikuValidator from "../components/HaikuValidator.svelte";
  import Posts from "../components/Posts.svelte";
  import { ready } from "@roxi/routify";
  import { updatePosts, filter, user } from "../stores";

  let posts = [];

  async function getPosts(filter) {
    const res = await fetch(`/api/posts?filter=${filter}`);
    const result = await res.json();
    posts = result.data;
    $ready();
  }

  async function getUserPosts(user) {
    const res = await fetch(`/api/posts?filter=user&username=${user}`);
    const result = await res.json();
    posts = result.data;
    $ready();
  }

  $: if ($updatePosts && $filter !== "my haikus") {
    getPosts($filter);
    $updatePosts = false;
  } else {
    getUserPosts($user);
    $updatePosts = false;
  }
</script>

<section class="mb-4 w-full max-w-2xl">
  <h1 class="mb-2 font-serif text-4xl font-bold text-center">haiku*</h1>

  <p>
    *a form of japanese poetry - a haiku expresses a single feeling or
    impression and contains three unrhymed lines of five, seven, and five
    syllables, respectively.
  </p>
</section>

<HaikuValidator />

<Posts {posts} />
