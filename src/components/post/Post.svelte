<script>
  import { getElapsedTime } from "../../helpers";
  import { isAuthenticated, user, csrf, updatePosts } from "../../stores";
  import { url } from "@roxi/routify";
  import CommentForm from "../comment/CommentForm.svelte";
  import { onMount, afterUpdate } from "svelte";
  import Comment from "../comment/Comment.svelte";
  import EditForm from "./EditForm.svelte";
  import { slide, fly } from "svelte/transition";
  import { media } from "svelte-match-media";

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

  onMount(() => {
    elapsedTime = getElapsedTime(time);
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
    <button class="flex gap-2 btn">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        class="w-6 h-6"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
        />
      </svg>
      {likes}
    </button>

    {#if !isSelected}
      <div class="flex items-center">
        <a
          href={$url("/:user/:id", { user: author, id: _id.$oid })}
          class="flex gap-2 link"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-6 h-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"
            />
          </svg>
          {comments.length}
        </a>
      </div>
    {/if}

    {#if $user !== author}
      <button class="btn">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-6 h-6"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M5 5a2 2 0 012-2h10a2 2 0 012 2v16l-7-3.5L5 21V5z"
          />
        </svg></button
      >
    {/if}

    {#if $isAuthenticated && $user === author}
      {#if isEditing}
        <button
          class="transition btn hover:bg-red-500"
          on:click={() => (isEditing = false)}
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-6 h-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg></button
        >
        <button
          class="transition btn hover:bg-green-500"
          type="submit"
          form="edit-form"
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-6 h-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M5 13l4 4L19 7"
            />
          </svg></button
        >
      {:else}
        <button
          class="btn"
          type="button"
          on:click={() => (isEditing = !isEditing)}
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-6 h-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
            />
          </svg></button
        >

        <button
          class="btn"
          on:click={() => (isDeleting = !isDeleting)}
          aria-label="Confirm deletion"
          ><svg
            xmlns="http://www.w3.org/2000/svg"
            class="w-6 h-6"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
            />
          </svg></button
        >
        {#if isDeleting && $media.desktop}
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

{#if isDeleting && $media.mobile}
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
