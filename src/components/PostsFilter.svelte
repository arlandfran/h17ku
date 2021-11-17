<script>
  import { isAuthenticated, filter, updatePosts } from "../stores";

  const onChangeHandler = () => {
    $filter = document.getElementById("filter").value;
    $updatePosts = true;
  };
</script>

<div class="flex justify-end w-full">
  <select
    name="filter"
    id="filter"
    class="p-2 bg-gray-800 rounded-sm cursor-pointer focus:outline-none focus:ring-2 focus:ring-black dark:ring-white"
    on:change={onChangeHandler}
  >
    {#if $isAuthenticated}
      <option value="my haikus" selected>my haikus</option>
    {/if}
    <option value="popular">popular</option>
    <option value="newest">newest</option>
  </select>
</div>
