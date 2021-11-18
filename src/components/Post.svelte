<script>
  import { getElapsedTime } from "../helpers";
  import { isAuthenticated, user } from "../stores";
  import { url } from "@roxi/routify";
  import CommentForm from "../components/CommentForm.svelte";
  import { onMount, afterUpdate } from "svelte";
  import Comment from "../components/Comment.svelte";
  import EditForm from "../components/EditForm.svelte";

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

  onMount(() => {
    elapsedTime = getElapsedTime(time);
  });

  afterUpdate(() => {
    time = new Date(posted_at.$date);
    elapsedTime = getElapsedTime(time);
  });
</script>

<div
  class="flex flex-col gap-y-4 px-4 py-4 w-full border-b border-black dark:border-gray-400"
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

  <div class="flex gap-4 items-center">
    <span>likes: {likes}</span>
    {#if $user !== author}
      <button class="btn"> save </button>
    {/if}

    {#if !isSelected}
      <a href={$url("/:user/:id", { user: author, id: _id.$oid })} class="link">
        {#if !comments.length}
          no comments
        {:else}
          {comments.length} comments
        {/if}
      </a>
    {/if}

    {#if $isAuthenticated && $user === author}
      {#if isEditing}
        <button class="btn" on:click={() => (isEditing = false)}>discard</button
        >
        <button class="btn" type="submit" form="edit-form">confirm</button>
      {:else}
        <button
          class="btn"
          type="button"
          on:click={() => (isEditing = !isEditing)}>edit</button
        >
        <button class="btn">delete</button>
      {/if}
    {/if}
  </div>
</div>

{#if isSelected}
  <CommentForm {author} {_id} />

  {#if comments.length}
    {#each [...comments].reverse() as comment}
      <Comment {...comment} />
    {/each}
  {/if}
{/if}
