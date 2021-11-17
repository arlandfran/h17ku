<script>
  import { getElapsedTime } from "../helpers";

  export let author;
  export let haiku;
  export let likes;
  export let created_at;

  const time = new Date(created_at.$date);
  const elapsedTime = getElapsedTime(time);
</script>

<div class="px-4 py-4 w-full border-b border-black dark:border-gray-400">
  <div class="mb-4 font-mono whitespace-pre-line">
    {haiku}
  </div>

  <div class="flex gap-4">
    <span
      >{author} • <time datetime={time.toISOString()}>{elapsedTime}</time></span
    >
    <span>likes: {likes}</span>
  </div>
</div>
