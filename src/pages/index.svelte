<script>
  import HaikuValidator from "../components/HaikuValidator.svelte";
  import Posts from "../components/Posts.svelte";
  import { ready } from "@roxi/routify";
  import { isPosting } from "../stores";

  let posts = [];

  getPosts();

  async function getPosts() {
    const res = await fetch("/api/posts");
    const result = await res.json();
    posts = result.data;
    $ready();
  }

  $: if ($isPosting) {
    getPosts();
    $isPosting = false;
  }
</script>

<section class="mb-4 w-full max-w-2xl">
  <h1 class="mb-2 text-4xl font-bold text-center dark:text-white">haiku*</h1>

  <p class="dark:text-white">
    *a form of japanese poetry - a haiku expresses a single feeling or
    impression and contains three unrhymed lines of five, seven, and five
    syllables, respectively.
  </p>
</section>

<HaikuValidator />

<Posts {posts} />
