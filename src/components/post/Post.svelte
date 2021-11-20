<script>
  import ToggleDelete from "../buttons/ToggleDelete.svelte";
  import ConfirmDelete from "../buttons/ConfirmDelete.svelte";
  import ToggleEdit from "../buttons/ToggleEdit.svelte";
  import CancelEdit from "../buttons/CancelEdit.svelte";
  import SubmitEdit from "../buttons/SubmitEdit.svelte";
  import CommentsLink from "../comment/CommentsLink.svelte";
  import LikeBtn from "../buttons/LikeBtn.svelte";
  import SaveBtn from "../buttons/SaveBtn.svelte";
  import EditPost from "./EditPost.svelte";

  import { goto } from "@roxi/routify";
  import { onMount, afterUpdate } from "svelte";
  import { slide, fly } from "svelte/transition";
  import { media } from "svelte-match-media";
  import { getElapsedTime } from "../../helpers";
  import { isAuthenticated, user, csrf, updatePosts } from "../../stores";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";

  export let _id;
  export let username;
  export let haiku;
  export let likes;
  export let posted_at;
  export let comments;
  export let edited;
  export let isSelected = false;

  let time = new Date(posted_at.$date);
  let elapsedTime;
  let isEditing;
  let isDeleting;
  let liked;
  let likesCount = likes.length;
  let commentsCount = comments.length;

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
  });

  const likeHandler = async () => {
    const response = await fetch(`/api/post?id=${_id.$oid}&like=${!liked}`, {
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
    const response = await fetch(`/api/post?id=${_id.$oid}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": $csrf,
      },
      credentials: "same-origin",
    });

    if (response.status === 204) {
      isDeleting = false;
      $updatePosts = true;
      if (isSelected) {
        $goto("/");
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
  class="flex relative flex-col gap-y-4 px-4 py-4 w-full border-b border-black dark:border-gray-400"
>
  <div>
    {username} •
    <time datetime={time.toISOString()}>{elapsedTime}</time>
    {#if edited}
      <span class="italic">edited</span>
    {/if}
  </div>

  {#if isEditing}
    <EditPost {_id} bind:isEditing bind:haiku />
  {:else}
    <div class="p-4 font-mono whitespace-pre-line">
      {haiku}
    </div>
  {/if}

  <div class="flex gap-4 items-center sm:gap-8">
    <LikeBtn {likesCount} {liked} {likeHandler} />

    {#if !isSelected}
      <CommentsLink {_id} {username} {commentsCount} />
    {/if}

    {#if $isAuthenticated && $user !== username}
      <SaveBtn id={_id.$oid} />
    {/if}

    {#if $isAuthenticated && $user === username}
      {#if isEditing}
        <CancelEdit bind:isEditing />
        <SubmitEdit form="edit-post-form" />
      {:else}
        <ToggleEdit bind:isEditing />

        <ToggleDelete bind:isDeleting />
        {#if isDeleting && !$media.smallMobile}
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

{#if isDeleting && $media.smallMobile}
  <div class="flex justify-center" transition:slide={{ duration: 200 }}>
    <ConfirmDelete {deleteHandler} />
  </div>
{/if}

<Toast />
