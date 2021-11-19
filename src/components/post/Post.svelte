<script>
  import DeleteBtn from "../buttons/DeleteBtn.svelte";
  import EditBtn from "../buttons/EditBtn.svelte";
  import CancelBtn from "../buttons/CancelBtn.svelte";
  import SubmitEditBtn from "../buttons/SubmitEditBtn.svelte";
  import CommentsLink from "../comment/CommentsLink.svelte";
  import LikeBtn from "../buttons/LikeBtn.svelte";
  import SaveBtn from "../buttons/SaveBtn.svelte";
  import Comment from "../comment/Comment.svelte";
  import CommentForm from "../comment/CommentForm.svelte";
  import EditForm from "./EditForm.svelte";

  import { onMount, afterUpdate } from "svelte";
  import { slide, fly } from "svelte/transition";
  import { media } from "svelte-match-media";
  import { getElapsedTime } from "../../helpers";
  import { isAuthenticated, user, csrf, updatePosts } from "../../stores";
  import { SvelteToast as Toast, toast } from "@zerodevx/svelte-toast";

  export let _id;
  export let author;
  export let haiku;
  export let likes;
  export let posted_at;
  export let comments;
  export let edited;
  export let isSelected = false;

  let time = new Date(posted_at.$date);
  let isEditing = false;
  let elapsedTime;
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
  });

  const deleteHandler = async () => {
    const response = await fetch(`/api/post?id=${_id.$oid}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": $csrf,
      },
      credentials: "same-origin",
    });

    if (response.status === 200) {
      isDeleting = false;
      $updatePosts = true;
    } else if (
      response.status === 400 &&
      result.msg === "The CSRF token has expired."
    ) {
      toast.push("session has expired, please refresh the page", {
        initial: 1,
        reversed: true,
        intro: { y: 64 },
        theme: {
          "--toastMinHeight": "2rem",
          "--toastPadding": "0 0.5rem",
          "--toastBarBackground": "transparent",
        },
      });
    }
  };
</script>

<div
  class="flex relative flex-col gap-y-4 px-4 py-4 w-full border-b border-black dark:border-gray-400"
>
  <div>
    {author} •
    <time datetime={time.toISOString()}>{elapsedTime}</time>
    {#if edited}
      <span class="italic">edited</span>
    {/if}
  </div>

  {#if isEditing}
    <EditForm {_id} bind:isEditing bind:haiku />
  {:else}
    <div class="font-mono whitespace-pre-line">
      {haiku}
    </div>
  {/if}

  <div class="flex gap-2 items-center md:gap-4">
    <LikeBtn id={_id.$oid} bind:likesCount bind:liked />

    {#if !isSelected}
      <CommentsLink id={_id.$oid} {author} comments={comments.length} />
    {/if}

    {#if $user !== author}
      <SaveBtn />
    {/if}

    {#if $isAuthenticated && $user === author}
      {#if isEditing}
        <CancelBtn bind:state={isEditing} />
        <SubmitEditBtn />
      {:else}
        <EditBtn bind:isEditing />

        <DeleteBtn bind:isDeleting />
        {#if isDeleting && !$media.smallMobile}
          <div
            class="flex justify-center"
            transition:fly={{ duration: 200, x: -10 }}
            on:click={deleteHandler}
          >
            <button class="btn danger">delete haiku?</button>
          </div>
        {/if}
      {/if}
    {/if}
  </div>
</div>

{#if isDeleting && $media.smallMobile}
  <div
    class="flex justify-center"
    transition:slide={{ duration: 200 }}
    on:click={deleteHandler}
  >
    <button class="btn danger">delete haiku?</button>
  </div>
{/if}

{#if isSelected}
  <CommentForm {author} {_id} />

  {#if comments.length}
    {#each [...comments].reverse() as comment}
      <Comment {...comment} />
    {/each}
  {/if}
{/if}

<Toast />
