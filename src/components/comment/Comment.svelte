<script>
  import { getElapsedTime } from "../../helpers";
  import { onMount, afterUpdate } from "svelte";
  import LikeBtn from "../buttons/LikeBtn.svelte";

  export let post_id;
  export let _id;
  export let username;
  export let comment;
  export let posted_at;
  export let likes;
  export let replies;

  let time = new Date(posted_at.$date);
  let elapsedTime;
  let liked;
  let count = likes.length;

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
    <span>{username}</span> •
    <time datetime={time.toISOString()}>{elapsedTime}</time>
  </div>
  <p>{comment}</p>

  <div class="flex gap-2 items-center md:gap-4">
    <LikeBtn
      bind:count
      bind:liked
      {post_id}
      comment_id={_id.$oid}
      isComment="true"
    />
  </div>
</div>
