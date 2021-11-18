<script>
  import { getElapsedTime } from "../helpers";
  import { isAuthenticated, user } from "../stores";
  import { url } from "@roxi/routify";
  import CommentForm from "../components/CommentForm.svelte";
  import { onMount, afterUpdate } from "svelte";

  export let _id;
  export let author;
  export let haiku;
  export let likes;
  export let created_at;
  export let isSelected = false;
  export let comments = [];

  let time = new Date(created_at.$date);
  let isEditing = false;
  let elapsedTime;

  onMount(() => {
    elapsedTime = getElapsedTime(time);
  });

  afterUpdate(() => {
    time = new Date(created_at.$date);
    elapsedTime = getElapsedTime(time);
  });

  const editHandler = () => (isEditing = !isEditing);
</script>

<div
  class="flex flex-col gap-y-4 px-4 py-4 w-full border-b border-black dark:border-gray-400"
>
  <div>
    <span
      >{author} •
      <time datetime={time.toISOString()}>{elapsedTime}</time></span
    >
  </div>

  {#if isEditing}
    textarea
  {:else}
    <div class="font-mono whitespace-pre-line">
      {haiku}
    </div>
  {/if}

  <div class="flex gap-4 items-center">
    <span>likes: {likes}</span>
    {#if $user !== author}
      <button class="btn"> save </button>
    {/if}

    {#if !isSelected}
      <a href={$url("/:user/:id", { user: author, id: _id.$oid })} class="link">
        comments
      </a>
    {/if}

    {#if $isAuthenticated && $user === author}
      <button class="btn" type="button" on:click={editHandler}>edit</button>
      <button class="btn">delete</button>
    {/if}
  </div>

  {#if isSelected}
    {#each comments as comment}
      {comment}
    {/each}
  {/if}
</div>

{#if isSelected}
  <CommentForm {author} />
{/if}
