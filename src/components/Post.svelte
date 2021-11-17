<script>
  import { getElapsedTime } from "../helpers";

  export let author;
  export let haiku;
  export let likes;
  export let created_at;

  const time = new Date(created_at.$date);
  const elapsedTime = getElapsedTime(time);
</script>

<div
  class="px-4 py-4 w-80 border-b border-black dark:border-white dark:border-b-2"
>
  <div class="mb-4 font-mono whitespace-pre-line">
    {haiku}
  </div>

  <div>
    {author} • {elapsedTime}
  </div>

  <div>
    likes: {likes}
  </div>
</div>
