<script>
  import { ready, url } from "@roxi/routify";
  import Posts from "../components/Posts.svelte";

  const slug = $url().slice(1);
  let posts = [];

  getData(slug);

  async function getData(username) {
    const response = await fetch(`/api/user?username=${username}`);

    const result = await response.json();

    if (response.status === 200) {
      posts = result.data;
      $ready();
    }
  }
</script>

<h1 class="mb-4 text-4xl font-bold dark:text-white">{slug}</h1>

<Posts {posts} />
