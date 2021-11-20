<script>
  import LikeBtn from "../buttons/LikeBtn.svelte";
  import ToggleEdit from "../buttons/ToggleEdit.svelte";
  import CancelEdit from "../buttons/CancelEdit.svelte";
  import SubmitEdit from "../buttons/SubmitEdit.svelte";
  import EditComment from "./EditComment.svelte";

  import { onMount, afterUpdate } from "svelte";
  import { getElapsedTime } from "../../helpers";
  import { csrf, user, isAuthenticated } from "../../stores";

  export let _id;
  export let username;
  export let comment;
  export let posted_at;
  export let likes;
  export let edited;

  let time = new Date(posted_at.$date);
  let elapsedTime;
  let isEditing;
  let liked;
  let likesCount = likes.length;

  onMount(() => {
    elapsedTime = getElapsedTime(time);
  });

  afterUpdate(() => {
    time = new Date(posted_at.$date);
    elapsedTime = getElapsedTime(time);
  });

  const likeHandler = async () => {
    const response = await fetch(`/api/comment?id=${_id.$oid}&like=${!liked}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": $csrf,
      },
      credentials: "same-origin",
      body: JSON.stringify({ username: $user }),
    });

    const result = await response.json();

    if (response.status === 200) {
      liked = result.liked;
      if (liked) {
        likesCount += 1;
      } else {
        likesCount -= 1;
      }
    } else if (
      response.status === 400 &&
      result.msg === "The CSRF token has expired."
    ) {
      toast.push("session has expired, please refresh the page", {
        initial: 1,
        reversed: true,
        intro: { y: 64 },
      });
    }
  };
</script>

<div
  class="flex flex-col gap-y-4 px-4 py-4 w-full border-b border-black dark:border-gray-400"
>
  <div>
    <span>{username}</span> •
    <time datetime={time.toISOString()}>{elapsedTime}</time>
    {#if edited}
      <span class="italic">edited</span>
    {/if}
  </div>

  {#if isEditing}
    <EditComment {_id} bind:isEditing bind:comment />
  {:else}
    <p class="p-4">{comment}</p>
  {/if}

  <div class="flex gap-4 items-center sm:gap-8">
    <LikeBtn {likesCount} {liked} {likeHandler} />

    {#if $isAuthenticated && $user === username}
      {#if isEditing}
        <CancelEdit bind:isEditing />
        <SubmitEdit form="edit-comment-form" />
      {:else}
        <ToggleEdit bind:isEditing />
      {/if}
    {/if}
  </div>
</div>
