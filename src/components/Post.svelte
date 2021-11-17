<script>
  export let author;
  export let haiku;
  export let likes;
  export let created_at;

  const time = new Date(created_at.$date).toDateString();
</script>

<div class="py-8 w-80 border-b-2 border-white dark:text-white">
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
