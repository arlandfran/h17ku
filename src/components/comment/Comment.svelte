<script>
  import LikeBtn from "../buttons/LikeBtn.svelte";
  import ToggleEdit from "../buttons/ToggleEdit.svelte";
  import CancelEdit from "../buttons/CancelEdit.svelte";
  import SubmitEdit from "../buttons/SubmitEdit.svelte";
  import EditComment from "./EditComment.svelte";
  import ToggleDelete from "../buttons/ToggleDelete.svelte";
  import ConfirmDelete from "../buttons/ConfirmDelete.svelte";

  import { onMount, afterUpdate } from "svelte";
  import { fly } from "svelte/transition";
  import { getElapsedTime } from "../../helpers";
  import { csrf, user, isAuthenticated, updateComments } from "../../stores";

  export let post_id;
  export let _id;
  export let username;
  export let comment;
  export let posted_at;
  export let likes;
  export let edited;

  let time = new Date(posted_at.$date);
  let elapsedTime;
  let isEditing;
  let isDeleting;
  let liked;
  let likesCount = likes.length;

  onMount(() => {
    elapsedTime = getElapsedTime(time);
    for (let i = 0; i < likes.length; i++) {
      if (likes[i] === $user) {
        liked = true;
      } else {
        liked = false;
      }
    }
  });

  afterUpdate(() => {
    time = new Date(posted_at.$date);
    elapsedTime = getElapsedTime(time);
    for (let i = 0; i < likes.length; i++) {
      if (likes[i] === $user) {
        liked = true;
      } else {
        liked = false;
      }
    }
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

  const deleteHandler = async () => {
    const response = await fetch(
      `/api/comment?pid=${post_id}&cid=${_id.$oid}`,
      {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": $csrf,
        },
        credentials: "same-origin",
      }
    );

    if (response.status === 204) {
      isDeleting = false;
      $updateComments = true;
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

        <ToggleDelete bind:isDeleting />
        {#if isDeleting}
          <div
            class="flex justify-center"
            transition:fly={{ duration: 200, x: -10 }}
          >
            <ConfirmDelete {deleteHandler} />
          </div>
        {/if}
      {/if}
    {/if}
  </div>
</div>
