<script>
  import { isAuthenticated, filter, updatePosts } from "../../stores";

  const onChangeHandler = () => {
    $filter = document.getElementById("filter").value;
    $updatePosts = true;
  };
</script>

<div class="self-end">
  <select
    name="filter"
    id="filter"
    class="cursor-pointer dropdown"
    on:change={onChangeHandler}
    aria-label="sort-filter"
  >
    {#if $isAuthenticated}
      <option label="my haikus" value="my-haikus" selected>my haikus</option>
    {/if}
    <option label="popular" value="popular">popular</option>
    <option label="newest" value="newest">newest</option>
  </select>
</div>
