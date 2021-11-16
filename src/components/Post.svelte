<script>
  export let author;
  export let haiku;
  export let likes;
</script>

<div class="w-full dark:text-white">
  <div>
    {haiku}
  </div>

  <div>
    author: {author}
  </div>

  <div>
    likes: {likes}
  </div>
</div>
