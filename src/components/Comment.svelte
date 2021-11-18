<script>
  import { getElapsedTime } from "../helpers";
  import { onMount, afterUpdate } from "svelte";

  export let username;
  export let comment;
  export let posted_at;

  let time = new Date(posted_at.$date);
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
    <span
      >{username} •
      <time datetime={time.toISOString()}>{elapsedTime}</time></span
    >
  </div>
  <div>{comment}</div>
</div>
