<script>
  export let author;
  export let haiku;
  export let likes;
  export let created_at;

  const time = new Date(created_at.$date).toDateString();
</script>

<div class="w-80 dark:text-white">
  <div>
    {haiku}
  </div>

  <div>
    {author} on {time}
  </div>

  <div>
    likes: {likes}
  </div>
</div>
