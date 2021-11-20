<script>
  import Post from "../../components/post/Post.svelte";
  import Comment from "../../components/comment/Comment.svelte";
  import CommentForm from "../../components/comment/CommentForm.svelte";

  import { onMount } from "svelte";
  import { params } from "@roxi/routify";
  import { updateComments } from "../../stores";

  let post;
  let comments = [];
  let isLoaded = false;

  onMount(async () => {
    await getPost();
    await getComments();
  });

  const getPost = async () => {
    const response = await fetch(`/api/post?id=${$params.id}`, {
      credentials: "same-origin",
    });

    const result = await response.json();
    if (response.status === 200) {
      post = await result.data;
      isLoaded = true;
    }
  };

  const getComments = async () => {
    const response = await fetch(`/api/comments?id=${$params.id}`, {
      credentials: "same-origin",
    });

    const result = await response.json();
    if (response.status === 200) {
      comments = await result.data;
    }
  };

  $: if ($updateComments) {
    getComments();
    $updateComments = false;
  }
</script>

<div class="grid gap-y-4 w-full max-w-2xl">
  {#if isLoaded}
    <Post {...post} isSelected="true" />

    <CommentForm _id={post._id} username={post.username} />

    {#each [...comments].reverse() as comment (comment._id.$oid)}
      <Comment {...comment} post_id={post._id.$oid} />
    {/each}
  {/if}
</div>
